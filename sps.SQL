USE [master]
GO

/****** Object:  StoredProcedure [dbo].[SPViewDatabasestoRestore]    Script Date: 4/24/2020 4:14:11 PM ******/
if OBJECT_ID('master..SPViewDatabasestoRestore') is not null
DROP PROCEDURE [dbo].[SPViewDatabasestoRestore]
GO

/****** Object:  StoredProcedure [dbo].[SPRestoration]    Script Date: 4/24/2020 4:14:11 PM ******/
IF OBJECT_ID('MASTER..SPRestoration') IS NOT NULL
DROP PROCEDURE [dbo].[SPRestoration]
GO
IF OBJECT_ID('MASTER..RunningStatus') IS NOT NULL
DROP TABLE [dbo].[RunningStatus]
GO


if OBJECT_ID('master..RestoredDBList') is not null
drop table RestoredDBList

Create Table RestoredDBList(DBName varchar(200))

IF OBJECT_ID('MASTER..DBlist') IS NOT NULL
DROP TABLE [dbo].[DBlist]
GO

CREATE TABLE [dbo].[DBlist](
	[DBlist] [varchar](500) NULL
) ON [PRIMARY]

GO


CREATE TABLE [dbo].[RunningStatus](
	[status] [int] NULL
) ON [PRIMARY]

GO
Insert into master.dbo.RunningStatus values (0)
go
/****** Object:  StoredProcedure [dbo].[SPRestoration]    Script Date: 4/23/2020 8:52:46 PM ******/

--exec SPRestoration 'D:\STUDY\DBA\Test\Backup\','D:\STUDY\DBA\Test\Data\','D:\STUDY\DBA\Test\log\'
--exec SPRestoration 'D:\STUDY\DBA\Test\Backup\','D:\STUDY\DBA\Test\Restore\Data\','D:\STUDY\DBA\Test\Restore\Log\'
CREATE procedure [dbo].[SPRestoration] (@BackupPath as varchar(500), @NewDatafilepath as varchar(500), @NewLogfilepath as varchar(500))
AS
BEGIN
SET NOCOUNT ON;
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
--2016 Version column added in #restorefilelistonly
--We need to manually restore databases with multiple files
--Existing database will be overwritten
--_New physical files will be created if mdf or ldf exists with same name.
update master.dbo.RunningStatus set [status] = 1;

declare @path varchar(5000)
Declare @DataPath varchar(500)
Declare @LogPath varchar(500)

set @path = (select @BackupPath)
set @DataPath = (select @NewDatafilepath)
Set @LogPath  = (select @NewLogfilepath)

if OBJECT_ID('tempdb..#files') is not null
DROP TABLE #files -- remove any previous instance

if OBJECT_ID('master..RestoredDBList') is not null
drop table RestoredDBList

Create Table RestoredDBList(DBName varchar(200))

CREATE TABLE #files(fname varchar(200),depth int, file_ int)
INSERT #files
EXECUTE master.dbo.xp_dirtree @path, 1, 1

--SELECT * FROM #files
DECLARE files CURSOR FOR
SELECT fname FROM #files where fname like '%.bak%'

DECLARE @name VARCHAR(256) -- database name 
OPEN files
FETCH NEXT FROM files INTO @name


WHILE @@FETCH_STATUS = 0  
BEGIN  
--select @name as '@name'
--select @@FETCH_STATUS as '@@FETCH_STATUS'

IF OBJECT_ID(N'tempdb..#filelistonly') IS NOT NULL
DROP TABLE #filelistonly
IF OBJECT_ID(N'tempdb..#headeronly') IS NOT NULL
DROP TABLE #headeronly

create table #filelistonly
(
LogicalName nvarchar(128) 
,PhysicalName nvarchar(260) 
,Type char(1) 
,FileGroupName nvarchar(128) 
,Size numeric(20,0) 
,MaxSize numeric(20,0),
Fileid tinyint,
CreateLSN numeric(25,0),
DropLSN numeric(25, 0),
UniqueID uniqueidentifier,
ReadOnlyLSN numeric(25,0),
ReadWriteLSN numeric(25,0),
BackupSizeInBytes bigint,
SourceBlocSize int,
FileGroupId int,
LogGroupGUID uniqueidentifier,
DifferentialBaseLSN numeric(25,0),
DifferentialBaseGUID uniqueidentifier,
IsReadOnly bit,
IsPresent bit, 
TDEThumbPrint varchar(50),
SnapshotURL varchar(500) NULL
)

Create Table #headeronly(
BackupName varchar(500)
,BackupDescription varchar(500)
,BackupType varchar(500)
,ExpirationDate varchar(500)
,Compressed varchar(500)
,Position varchar(500)
,DeviceType varchar(500)
,UserName varchar(500)
,ServerName varchar(500)
,DatabaseName varchar(500)
,DatabaseVersion varchar(500)
,DatabaseCreationDate varchar(500)
,BackupSize varchar(500)
,FirstLSN varchar(500)
,LastLSN varchar(500)
,CheckpointLSN varchar(500)
,DatabaseBackupLSN varchar(500)
,BackupStartDate varchar(500)
,BackupFinishDate varchar(500)
,SortOrder varchar(500)
,CodePage varchar(500)
,UnicodeLocaleId varchar(500)
,UnicodeComparisonStyle varchar(500)
,CompatibilityLevel varchar(500)
,SoftwareVendorId varchar(500)
,SoftwareVersionMajor varchar(500)
,SoftwareVersionMinor varchar(500)
,SoftwareVersionBuild varchar(500)
,MachineName varchar(500)
,Flags varchar(500)
,BindingID varchar(500)
,RecoveryForkID varchar(500)
,Collation varchar(500)
,FamilyGUID varchar(500)
,HasBulkLoggedData varchar(500)
,IsSnapshot varchar(500)
,IsReadOnly varchar(500)
,IsSingleUser varchar(500)
,HasBackupChecksums varchar(500)
,IsDamaged varchar(500)
,BeginsLogChain varchar(500)
,HasIncompleteMetaData varchar(500)
,IsForceOffline varchar(500)
,IsCopyOnly varchar(500)
,FirstRecoveryForkID varchar(500)
,ForkPointLSN varchar(500)
,RecoveryModel varchar(500)
,DifferentialBaseLSN varchar(500)
,DifferentialBaseGUID varchar(500)
,BackupTypeDescription varchar(500)
,BackupSetGUID varchar(500)
,CompressedBackupSize varchar(500)
,Containment varchar(500)
,KeyAlgorithm varchar(500)
,EncryptorThumbprint varchar(500)
,EncryptorType varchar(500)
)



insert into #filelistonly
EXEC ('restore filelistonly from disk = ''' +@path+@name + '''')

insert into #headeronly
EXEC ('restore headeronly from disk = ''' +@path+@name + '''')
--restore headeronly from disk = 'F:\DBRefresh\BackupsProd\FDC_backup_2020_02_18_190515_6942838.bak'

--Select DatabaseName from #headeronly
--select * from #filelistonly
Declare @RestoreString as Varchar(max)
Declare @NRestoreString as NVarchar(max)
DECLARE @LogicalName  as varchar(75)
Declare @counter as int
Declare @rows as int
Declare @DataFile as varchar(500)
Declare @LogFile varchar(500)
Declare @Options varchar(500)
Declare @DBName varchar(500)

Declare @Single nvarchar(500)
Declare @multi nvarchar(500)
Set @DBName = (Select DatabaseName from #headeronly)
set @Options = ', recovery, replace;'



--select @rows = COUNT(*) from #filelistonly
--select @Rows as [These are the number of rows]

Declare @Datafilecount as INT
Declare @Logfilecount as INT
set @Datafilecount = (Select count(1) from #filelistonly where [Type]='D')
--Select @Datafilecount as '@Datafilecount'
set @Logfilecount=(Select count(1) from #filelistonly where [Type]='L')
--Select @Logfilecount as '@Logfilecount'


IF (@Datafilecount>1 OR @Logfilecount>1)
BEGIN
Select 'There are more than 1 data or log files for Database: '+@DBName+' Please restore this Database manually'
--print 'Skipping this database restoration...................'
GOTO SKIPRESTORE
END
Set @DataFile = (Select logicalname as DataFile from #filelistonly where [Type]='D')
Set @LogFile =  (Select logicalname as LogFile from #filelistonly where [Type]='L')

--Select @DataFile
--Select @LogFile

Declare @mdffile varchar(max)
Declare @ldffile varchar(max)
set @mdffile = (select @DataPath+@DataFile+'.mdf')
--select @mdffile as '@mdffile'
set @ldffile = (Select @LogPath+@LogFile+'.ldf')
--select @ldffile as '@ldffile'

IF OBJECT_ID(N'tempdb..#mdf') IS NOT NULL
DROP TABLE #mdf
IF OBJECT_ID(N'tempdb..#ldf') IS NOT NULL
DROP TABLE #ldf

--Check for exiting mdf files
--print 'checking for existing mdf file..................'
CREATE TABLE #mdf(mdfname varchar(200),depth int, file_ int)
INSERT #mdf
EXECUTE master.dbo.xp_dirtree @DataPath, 1, 1

declare @fullmdfname varchar(500)
set @fullmdfname = (select @DataPath+mdfname from #mdf where mdfname like '%'+@DataFile+'.mdf%')
--select @fullmdfname as '@fullmdfname'
--select @mdffile as '@mdffile'


--check for existing ldf files
--print 'checking for existing ldf file..................'
CREATE TABLE #ldf(ldfname varchar(200),depth int, file_ int)

INSERT #ldf
EXECUTE master.dbo.xp_dirtree @logPath, 1, 1

declare @fullldfname varchar(500)
set @fullldfname = (select @LogPath+ldfname from #ldf where ldfname like '%'+@logfile+'.ldf%')
--select @fullldfname as '@fullldfname'
--select @ldffile as '@ldffile'

--Check for same physical files associated to different database
if exists(select * from sys.sysaltfiles where (filename=@mdffile OR filename=@ldffile))
BEGIN
GOTO CREATENEWFILES
END
ELSE
GOTO DoNotCreateNewFiles

if (@fullmdfname=@mdffile) OR (@fullldfname=@ldffile)
BEGIN
--Print 'mdf/ ldf file names matching with destination files names'
CREATENEWFILES:
--Print 'mdf or ldf files exits with same name ! Creating new mdf and ldf files with _new names'
set @RestoreString = 'RESTORE DATABASE ['+@DBName+'] FROM DISK = N'''+@path+@name+''''
+' with move '''+ @DataFile + '''' + ' TO N'''+@DataPath+''+@DBName + '_new.mdf'''+' ,'
+ 'move  N''' + @LogFile + '''' + ' TO N'''+@LogPath+''+@DBName + '_log_new.ldf' +''''+@Options+''
set @NRestoreString=@RestoreString
END
ELSE
BEGIN
DoNotCreateNewFiles:
--print 'No need to create _new mdf or ldf files'
set @RestoreString = 'RESTORE DATABASE ['+@DBName+'] FROM DISK = N'''+@path+@name+''''
+' with move '''+ @DataFile + '''' + ' TO N'''+@DataPath+''+@DBName + '.mdf'''+' ,'
+ 'move  N''' + @LogFile + '''' + ' TO N'''+@LogPath+''+@DBName + '_log.ldf' +''''+@Options+''
set @NRestoreString=@RestoreString
END

If exists (Select name from sys.databases where name = @DBName)
BEGIN
--Print 'Database '+@DBname+' already exists ! setting to single_user mode before overwritting it'
Set @Single = 'ALTER database '+@dbname+' set single_user with rollback immediate';
--print @Single
exec sp_executesql @Single;
END
--print @NRestoreString
--Select 'starting restoration for :'+@DBName
BEGIN try
exec sp_executesql @NRestoreString;
END try
begin catch
GOTO SKIPRESTORE
end catch
BEGIN
Insert into RestoredDBlist values (@DBName);
END
Set @multi = 'ALTER database '+@dbname+' set multi_user';
--print @multi
exec sp_executesql @multi;

SKIPRESTORE:
FETCH NEXT FROM files INTO @name;

END
CLOSE files
DEALLOCATE files

update RunningStatus set [status] = 0;
END
GO

/****** Object:  StoredProcedure [dbo].[SPViewDatabasestoRestore]    Script Date: 4/24/2020 4:14:11 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


--exec SPViewDatabasestoRestore 'D:\STUDY\DBA\Test\Backup\' --,'D:\STUDY\DBA\Test\Restore\Data\','D:\STUDY\DBA\Test\Restore\Log\'
CREATE procedure [dbo].[SPViewDatabasestoRestore] (@BackupPath as varchar(500))
AS
BEGIN
--2016 Version column added in #restorefilelistonly
--We need to manually restore databases with multiple files
--Existing database will be overwritten
--_New physical files will be created if mdf or ldf exists with same name.

declare @path varchar(5000)
set @path = (select @BackupPath)


if OBJECT_ID('tempdb..#files') is not null
DROP TABLE #files -- remove any previous instance
IF OBJECT_ID(N'master..headeronly') IS NOT NULL
DROP TABLE headeronly
IF OBJECT_ID(N'master..DBlist') IS NOT NULL
DROP TABLE DBlist

Create Table headeronly(
BackupName varchar(500)
,BackupDescription varchar(500)
,BackupType varchar(500)
,ExpirationDate varchar(500)
,Compressed varchar(500)
,Position varchar(500)
,DeviceType varchar(500)
,UserName varchar(500)
,ServerName varchar(500)
,DatabaseName varchar(500)
,DatabaseVersion varchar(500)
,DatabaseCreationDate varchar(500)
,BackupSize varchar(500)
,FirstLSN varchar(500)
,LastLSN varchar(500)
,CheckpointLSN varchar(500)
,DatabaseBackupLSN varchar(500)
,BackupStartDate varchar(500)
,BackupFinishDate varchar(500)
,SortOrder varchar(500)
,CodePage varchar(500)
,UnicodeLocaleId varchar(500)
,UnicodeComparisonStyle varchar(500)
,CompatibilityLevel varchar(500)
,SoftwareVendorId varchar(500)
,SoftwareVersionMajor varchar(500)
,SoftwareVersionMinor varchar(500)
,SoftwareVersionBuild varchar(500)
,MachineName varchar(500)
,Flags varchar(500)
,BindingID varchar(500)
,RecoveryForkID varchar(500)
,Collation varchar(500)
,FamilyGUID varchar(500)
,HasBulkLoggedData varchar(500)
,IsSnapshot varchar(500)
,IsReadOnly varchar(500)
,IsSingleUser varchar(500)
,HasBackupChecksums varchar(500)
,IsDamaged varchar(500)
,BeginsLogChain varchar(500)
,HasIncompleteMetaData varchar(500)
,IsForceOffline varchar(500)
,IsCopyOnly varchar(500)
,FirstRecoveryForkID varchar(500)
,ForkPointLSN varchar(500)
,RecoveryModel varchar(500)
,DifferentialBaseLSN varchar(500)
,DifferentialBaseGUID varchar(500)
,BackupTypeDescription varchar(500)
,BackupSetGUID varchar(500)
,CompressedBackupSize varchar(500)
,Containment varchar(500)
,KeyAlgorithm varchar(500)
,EncryptorThumbprint varchar(500)
,EncryptorType varchar(500)
)

CREATE TABLE #files(fname varchar(200),depth int, file_ int)
INSERT #files
EXECUTE master.dbo.xp_dirtree @path, 1, 1

--SELECT * FROM #files
DECLARE files CURSOR FOR
SELECT fname FROM #files where fname like '%.bak%'

DECLARE @name VARCHAR(256) -- Backup file name 
OPEN files
FETCH NEXT FROM files INTO @name

WHILE @@FETCH_STATUS = 0  
BEGIN 

insert into headeronly
EXEC ('restore headeronly from disk = ''' +@path+@name + '''')

FETCH NEXT FROM files INTO @name

END
CLOSE files
DEALLOCATE files
Select distinct DatabaseName as 'DBlist' into DBlist from headeronly
Select * from DBlist 

END
GO

