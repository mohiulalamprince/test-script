import psycopg2

def dbConnect():
	DB_NAME = "crowdcoop-test-server-fresh1"
	USERNAME = "postgres"
	PASSWORD = "postgres"

	HOST = "127.0.0.1"
	PORT = "5432"

	try:
		conn = psycopg2.connect(database=DB_NAME, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
		return True, conn
	except Exception, ex:
		print "Exception during database connection: " + str(ex)
		return False, None


TABLE_LIST = ['client_client', 'client_clientauditlogentry', 'client_clientmanagement', 'client_clientmanagementauditlogentry', 'custom_user_userclientsharerole', 'custom_user_userclientshareroleauditlogentry', 'share_share', 'share_shareauditlogentry', 'share_sharehistory', 'share_sharehistoryauditlogentry', 'share_sharehistorydocuments', 'share_sharehistorydocumentsauditlogentry']

SPECIAL_TABLE_LIST = ['oauth2_provider_accesstoken', 'oauth2_provider_refreshtoken', 'custom_user_userprofileauditlogentry', 'custom_user_userprofile', 'auth_user']

status, conn = dbConnect()
if status:
	print "Opened database successfully"
	cur = conn.cursor()

	for table in TABLE_LIST:
		try:
			query_string = "DELETE from " + table + ";"
			cur.execute(query_string)
			print "Total number of rows deleted :", cur.rowcount
			print "query: " + query_string
		except Exception, ex:
			print "Exception during deleting data: " + str(ex)

	conn.commit()
	
	for table in SPECIAL_TABLE_LIST:
		try:
			query_string = "DELETE from " + table;
			if table == "auth_user":
				query_string = query_string + " where id>1;"
			else:
				query_string = query_string + " where user_id>1"

			cur.execute(query_string)
			print "Total number of rows deleted :", cur.rowcount
			print "query: " + query_string
		except Exception, ex:
			print "Exception during deleting data: " + str(ex)
	

	conn.commit()
	#print "Closing db connection... ..."
	#conn.close()
	#print "Closed"

else:
	print "Noting to do..."

