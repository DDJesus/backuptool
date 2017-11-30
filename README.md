# backuptool

CLI Tool used to quickly back-up/restore Microsoft SQL Server Database's.

You will need to do two things:

  1. If restoring a backup, place the backup file in the projects working directory.
    
    Example:
      
      C:\Python\backuptools\file_to_restore.bak
  
  2. Fill out the information in config.py. You will need:
      + Server Name
      + If backing up a database, the name of the database you wish to back up
      + Username of SQL Server user with permissions to backup/restore
      + Password of User
    
Run the program by opening a command prompt (with elevated permissions) in the projects directory. Currently there are two commands you can use:

  1. -b: Backup
    
    Example:
      
      python backuptool.py -b
    
   You will be prompted to supply the filename.
   
  2. -r: Restore
    
    Example:
      
      python backuptool.py -r
    
   You will be prompted to supply the filename and restored Database's name. Make sure you include the .bak extension with the file name.

There is also a help.txt file if you are curious about more, or you can use the -h flag to view help from the command line.

I hope to scope this out to include MySQL, Postgresql, and other RDBMS, but for now it only does MSSQL. I know it also works on 2008 and 2012 SQL Server, have yet to test on 2014+. Hope to continue building on this, just depends on how much time I have free from work.
