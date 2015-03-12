#!/home/nsadmin/Documents/Praneet/Codes/Research_data/env python
import MySQLdb
#GRANT ALL PRIVILEGES ON 172.16.96.175.app_info TO app_info@192.168.104.243 IDENTIFIED BY "abc12345"
db=MySQLdb.connect("172.16.96.175","releaseOfficer","abc12345","app_info")
cursor=db.cursor()
roll = "SELECT `id`, `AppName`, `roleAuthBased`  FROM `research_data` WHERE `roleAuthBased` != 'Yes' AND `roleAuthBased` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(roll)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'w')
   print >>a,"\n............Output for RoleBased Auth........ \n"
   for row in results:
		App_ID = row[0]
		App_Name = row[1]
		Roll_based_Auth = row[2]
      # Now print fetched result
		print >>a,"App_ID=%s "",App_Name=%s "",Roll_based_Auth=%s" % \
		(App_ID, App_Name, Roll_based_Auth)
	#a.close()
except:
   print "Error: unable to fetch RoleBased Auth."
  
multi = "SELECT `id`, `AppName`, `multifactor`  FROM `research_data` WHERE `multifactor` != 'Yes' AND `multifactor` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(multi)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for multifactor........ \n"
   for row in results:
		App_ID = row[0]
		App_Name = row[1]
		multifactor = row[2]
      # Now print fetched result
		print >>a,"App_ID=%s "",App_Name=%s "",multifactor=%s" % \
		(App_ID, App_Name, multifactor)
	#a.close()      
except:
   print "Error: unable to fetch multifactor"
   
sso = "SELECT id, AppName,SSOADhooks FROM `research_data` WHERE (`SSOADhooks` not like '%AD/LDAP%' and `SSOADhooks` not like '%OpenID%' and `SSOADhooks` not like '%SAML%' and `SSOADhooks` not like '%NS%' and `SSOADhooks` not like '%Facebook%' and `SSOADhooks` not like '%Twitter%' and `SSOADhooks` not like '%OAuth%') and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(sso)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for SSO..................... \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      SSOADhooks = row[2]
      # Now print fetched result
      print >>a, "App_ID=%s "",App_Name=%s "",SSOADhooks=%s" % \
      (App_ID, App_Name, SSOADhooks)
	#a.close()  
except:
   print "Error: unable to fetch data for SSO"

gran = "SELECT `id`, `AppName`, `granularpolicies`  FROM `research_data` WHERE `granularpolicies` != 'Yes' AND `granularpolicies` != 'No' AND completionstatus like '%APP ALL COMPLETE %'"
try:
   # Execute the SQL command
   cursor.execute(gran)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for Granularpolicies....... \n"
   for row in results:
	  App_ID = row[0]
	  App_Name = row[1]
	  Granularpoli = row[2]
      # Now print fetched result
	  print >>a,"App_ID=%s "",App_Name=%s "",Granularpolicies=%s" % \
	  (App_ID, App_Name, Granularpoli)	  
	#a.close()  
except:
   print "Error: unable to fetch Granular Auth."
   
drest = "SELECT id, AppName,devicerestrictions FROM `research_data` WHERE (`devicerestrictions` not like '%ANDROID%' and `devicerestrictions` not like '%IOS%' and `devicerestrictions` not like '%BLACKBERRY%' and `devicerestrictions` not like '%NS%' and `devicerestrictions` not like '%WINDOWS%' and `devicerestrictions` not like '%DESKTOP%' and `devicerestrictions` not like '%Browser%'and `devicerestrictions` not like '%ALL%' ) and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(drest)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt','a')
   print >>a,"\n ............Output for Device restrictions....... \n"
   for row in results:
		App_ID = row[0]
		App_Name = row[1]
		Devicerestrict = row[2]
      # Now print fetched result
		print >>a, "App_ID=%s "",App_Name=%s "",devicerestrictions=%s" % \
		(App_ID, App_Name, Devicerestrict)
	#a.close()  	  
except:
	print "Error: unable to fetch data from devicerestrictions"
	
ipfilter = "SELECT `id`, `AppName`, `ipfilter`  FROM `research_data` WHERE `ipfilter` != 'Yes' AND `ipfilter` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(ipfilter)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for ipfilter........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      ipfilter = row[2]
	  # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",ipfilter=%s" % \
      (App_ID, App_Name, ipfilter)
	      
except:
   print "Error: unable to fetch data for ipfilter"
   
epass = "SELECT `id`, `AppName`, `EnforcePassword`  FROM `research_data` WHERE `EnforcePassword` != 'Yes' AND `EnforcePassword` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(epass)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for EnforcePassword........ \n"
   for row in results:
          App_ID = row[0]
	  App_Name = row[1]
	  EnforcePassword = row[2]
      # Now print fetched result
	  print >>a,"App_ID=%s "",App_Name=%s "",EnforcePassword=%s" % \
          (App_ID, App_Name, EnforcePassword)
	      
except:
   print "Error: unable to fetch data from EnforcePassword"

enrest = "SELECT id, AppName,encryptionDataRest FROM `research_data` WHERE (`encryptionDataRest` not like '%AUR%' and `encryptionDataRest` not like '%AES%' and `encryptionDataRest` not like '%DES%' and `encryptionDataRest` not like '%NS%' and `encryptionDataRest` not like '%RSA%' and `encryptionDataRest` not like '%BitLocker%' and `encryptionDataRest` not like '%Blowfish%' and `encryptionDataRest` not like '%NA%' ) and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(enrest)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   b=open('dump.txt', 'a')
   print >>a,"\n............Output for EncryptionDataRest........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      encryptionDataRest = row[2]
      # Now print fetched result
      print >>b, "App_ID=%s "",App_Name=%s "",encryptionDataRest=%s" % \
      (App_ID, App_Name, encryptionDataRest)
	  	  
except:
   print "Error: unable to fetch data from EncryptionDataRest"

trans = "SELECT `id`, `AppName`, `encryptionInTransit`  FROM `research_data` WHERE `encryptionInTransit` != 'Yes' AND `encryptionInTransit` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(trans)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for EncryptionInTransit........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      encryptionInTransit = row[2]
	  # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",encryptionInTransit=%s" % \
      (App_ID, App_Name, encryptionInTransit)
	      
except:
   print "Error: unable to fetch data from encryptionInTransit"

tenan = "SELECT `id`, `AppName`, `datapertenancy`  FROM `research_data` WHERE `datapertenancy` != 'Yes' AND `datapertenancy` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(tenan)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for Datapertenancy........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      datapertenancy = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",datapertenancy=%s" % \
      (App_ID, App_Name, datapertenancy)
	      
except:
   print "Error: unable to fetch data from datapertenancy"
    
etena = "SELECT `id`, `AppName`, `EncryptTenantKey`  FROM `research_data` WHERE `EncryptTenantKey` != 'Yes' AND `EncryptTenantKey` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(etena)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"............Output for EncryptTenantKey........ \n"
   for row in results:
	  App_ID = row[0]
	  App_Name = row[1]
	  EncryptTenantKey = row[2]
	  print >>a,"App_ID=%s "",App_Name=%s "",EncryptTenantKey=%s" % \
          (App_ID, App_Name, EncryptTenantKey)
	      
except:
   print "Error: unable to fetch data from EncryptTenantKey"

dclass = "SELECT `id`, `AppName`, `dataClassification`  FROM `research_data` WHERE `dataClassification` != 'Yes' AND `dataClassification` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(dclass)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for DataClassification........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      dataClassification = row[2]
	  # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",dataClassification=%s" % \
      (App_ID, App_Name, dataClassification)
	      
except:
   print "Error: unable to fetch dataClassification"   

ccapa = "SELECT `id`, `AppName`, `classificationCapabilities`  FROM `research_data` WHERE `classificationCapabilities` != 'Yes' AND `classificationCapabilities` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(ccapa)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for ClassificationCapabilities........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      classificationCapabilities = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",classificationCapabilities=%s" % \
      (App_ID, App_Name, classificationCapabilities)
	      
except:
   print "Error: unable to fetch data from classificationCapabilities"
 
dreco = "SELECT `id`, `AppName`, `disasterecovery`  FROM `research_data` WHERE `disasterecovery` != 'Yes' AND `disasterecovery` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(dreco)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for disasterecovery........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      Disasterecov = row[2]
      # Now print fetched result    
      print >>a,"App_ID=%s "",App_Name=%s "",disasterecovery=%s" % \
      (App_ID, App_Name, disasterecovery)
	      
except:
   print "Error: unable to fetch data from disasterecovery"

hgeo = "SELECT `id`, `AppName`, `hostinggeo`  FROM `research_data` WHERE `hostinggeo` != 'Yes' AND `hostinggeo` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(hgeo)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a') 
   print >>a,"\n............Output for Hostinggeo........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      Hostingg = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",hostinggeo=%s" % \
      (App_ID, App_Name, Hostingg)
	      
except:
   print "Error: unable to fecth data 1234"   
   
geoba = "SELECT `id`, `AppName`, `hostinggeoback`  FROM `research_data` WHERE `hostinggeoback` != 'Yes' AND `hostinggeoback` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(geoba)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for Hostinggeobackup........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      HostinggeoB = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",hostinggeoback=%s" % \
      (App_ID, App_Name, HostinggeoB)
	      
except:
   print "Error: unable to fetch data from hostinggeoback"   

dcert = "SELECT id, AppName,datacenterCert FROM `research_data` WHERE (`datacenterCert` not like '%ISO27001%' and `datacenterCert` not like '%SAS70/SSAE-16%' and `datacenterCert` not like '%SOC-1%' and `datacenterCert` not like '%NS%' and `datacenterCert` not like '%SOC-2%' and `datacenterCert` not like '%SOC-3%' and `datacenterCert` not like '%NA%' ) and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(dcert)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for DatacenterCert........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      DatacenterC = row[2]
      # Now print fetched result 
      print >>a, "App_ID=%s "",App_Name=%s "",datacenterCert=%s" % \
      (App_ID, App_Name, DatacenterC)	  
	  
except:
   print "Error: unable to fetch data from datacenterCert"   
  
ccert = "SELECT id, AppName,complianceCert FROM `research_data` WHERE (`complianceCert` not like '%HIPAA%' and `complianceCert` not like '%Safe Harbor%' and `complianceCert` not like '%TRUSTe%' and `complianceCert` not like '%NS%' and `complianceCert` not like '%PCIDSS20%' and `complianceCert` not like '%GAPP%' and `complianceCert` not like '%COBIT%' ) and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(ccert)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for ComplianceCert........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      ComplianceC = row[2]
      # Now print fetched result
      print >>a, "App_ID=%s "",App_Name=%s "",ComplianceC=%s" % \
      (App_ID, App_Name, ComplianceC)
	  	  
except:
   print "Error: unable to fetch data from ComplianceCert"
   
infra = "SELECT `id`, `AppName`, `infrahealth`  FROM `research_data` WHERE `infrahealth` != 'Yes' AND `infrahealth` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(infra)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for infrahealth........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      Infra = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",infrahealth=%s" % \
      (App_ID, App_Name, Infra)
	      
except:
   print "Error: unable to fetch For infrahealth"   
     
ntime = "SELECT `id`, `AppName`, `notificationLeadTime`  FROM `research_data` WHERE `notificationLeadTime` != 'Yes' AND `notificationLeadTime` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(ntime)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for NotificationLeadTime........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      NotificationLead = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",notificationLeadTime=%s" % \
      (App_ID, App_Name, NotificationLead)
	      
except:
   print "Error: unable to fetch data for notificationLeadTime"   
   
adlog = "SELECT `id`, `AppName`, `adminauditlogs`  FROM `research_data` WHERE `adminauditlogs` != 'Yes' AND `adminauditlogs` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(adlog)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for Adminauditlogs........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      Adminauditlog = row[2]
      # Now print fetched result 
      print >>a,"App_ID=%s "",App_Name=%s "",adminauditlogs=%s" % \
      (App_ID, App_Name, Adminauditlog)
	      
except:
   print "Error: unable to fetch data for adminauditlogs"   
   
ulogs = "SELECT `id`, `AppName`, `userauditlogs`  FROM `research_data` WHERE `userauditlogs` != 'Yes' AND `userauditlogs` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(ulogs)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for Userauditlogs........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      Userauditlog = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",userauditlogs=%s" % \
      (App_ID, App_Name, Userauditlog)
	      
except:
   print "Error: unable to fetch data for userauditlogs"   
     
dlogs = "SELECT `id`, `AppName`, `dataauditlogs`  FROM `research_data` WHERE `dataauditlogs` != 'Yes' AND `dataauditlogs` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(dlogs)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for Dataauditlogs........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      Dataauditlog = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",dataauditlogs=%s" % \
      (App_ID, App_Name, Dataauditlog)
	      
except:
   print "Error: unable to fetch data for dataauditlogs"   
   
fsz = "SELECT `id`, `AppName`, `FS`  FROM `research_data` WHERE `FS` != 'Yes' AND `FS` != 'No' AND completionstatus like '%APP ALL COMPLETE %' "
try:
   # Execute the SQL command
   cursor.execute(fsz)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"............Output for FS..................... \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      FSIZ = row[2]
      # Now print fetched result
      print >>a,"App_ID=%s "",App_Name=%s "",FS=%s" % \
      (App_ID, App_Name, FSIZ)
	      
except:
   print "Error: unable to fetch data for File sharing" 
   
fsize = "SELECT id, AppName,FSsize FROM `research_data` WHERE (`FSsize` not like '%5to10%' and `FSsize` not like '%gt10%' and `FSsize` not like '%lt5%' and `FSsize` not like '%NA%' and `FSsize` not like '%No%') and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(fsize)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for F Size.................. \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      size = row[2]
      # Now print fetched result
      print >>a, "App_ID=%s "",App_Name=%s "",FSsize=%s" % \
      (App_ID, App_Name, size)
	  	  
except:
   print "Error: unable to fetch data for FSsize"     

draspg = "SELECT id, AppName,DataRetentionAtSaaSPostDereg FROM `research_data` WHERE (`DataRetentionAtSaaSPostDereg` not like '%gt1month%' and `DataRetentionAtSaaSPostDereg` not like '%lt1month%' and `DataRetentionAtSaaSPostDereg` not like '%lt1week%' and `DataRetentionAtSaaSPostDereg` not like '%NS%' and `DataRetentionAtSaaSPostDereg` not like '%Unspecified%') and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(draspg)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for DataRetentionAtSaaSPostDereg........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      DataRetentionAtSaaSPost = row[2]
      # Now print fetched result
      print >>a, "App_ID=%s "",App_Name=%s "",DataRetentionAtSaaSPostDereg=%s" % \
      (App_ID, App_Name, DataRetentionAtSaaSPost)
	  	  
except:
   print "Error: unable to fetch data from DataRetention"  

downer = "SELECT id, AppName,dataOwnership FROM `research_data` WHERE (`dataOwnership` not like 'Yes' and `dataOwnership` not like '%No%' and `dataOwnership` not like '%Unspecified%') and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(downer)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for DataOwnership........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      DataOwner = row[2]
      # Now print fetched result
      print >>a, "App_ID=%s "",App_Name=%s "",dataOwnership=%s" % \
      (App_ID, App_Name, DataOwner)
	  	  
except:
   print "Error: unable to fetch data from dataOwnership"     
   
dava = "SELECT id, AppName,DataAvailabilityPostDereg FROM `research_data` WHERE (`DataAvailabilityPostDereg` not like '%immediately%' and `DataAvailabilityPostDereg` not like '%Unspecified%' and `DataAvailabilityPostDereg` not like '%NS%') and completionStatus like '%APP ALL COMPLETE %'" 
try:
   # Execute the SQL command
   cursor.execute(dava)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   a=open('dump.txt', 'a')
   print >>a,"\n............Output for DataAvailabilityPostDereg........ \n"
   for row in results:
      App_ID = row[0]
      App_Name = row[1]
      DataAvailabilityPost = row[2]
      # Now print fetched result
      print >>a, "App_ID=%s "",App_Name=%s "",DataAvailabilityPostDereg=%s" % \
      (App_ID, App_Name, DataAvailabilityPost)	  
	  
except:
   print "Error: unable to fetch data from DataAvailability"

a=open('dump.txt', 'a')
print >>a,"Best Regards"  
print >>a,"B.S.Praneet"
print >>a,"NetSkope Software"
cursor.close()
# close the connection
a.close()
db.close ()
