# netflix userbase

mysql_queries = ['select User_ID,Join_Date,Country,Age from netflix_userbase where Subscription_Type= "Basic"',
                 "INSERT INTO netflix_userbase (User_ID, Subscription_Type, Monthly_Revenue, Join_Date, Last_Payment_Date, Country, Age, Gender, Device, Plan_Duration) VALUES (2501, 'Basic', 18, '2022-08-31', '2023-07-21', 'United States', 33, 'Female', 'Smart TV', '1 Month') ON DUPLICATE KEY UPDATE User_ID=2502;",
                 "UPDATE netflix_userbase SET Age = 30 WHERE User_ID = 1;",
                 "DELETE FROM netflix_userbase WHERE User_ID = 2;",
                  'SELECT a.Join_Date, b.Last_Payment_Date FROM netflix_userbase AS a LEFT JOIN netflix_userbase AS b ON a.User_ID = b.User_ID;']
mongodb_queries = ['db.netflix_userbase.find({"Subscription_Type": "Basic"})',
                   'db.netflix_userbase.insertOne({ "User_ID": 2501, "Subscription_Type": "Basic" , "Monthly_Revenue": 18, "Join_Date": "2022-08-31", "Last_Payment_Date": "2023-07-21" , "Country": "United States", "Age": 33 , "Gender": "Female" , "Device": "Smart TV", "Plan_Duration": "1 Month"})',
                   'db.netflix_userbase.updateOne({"User_ID" :1}, {"$set": {"Age":30} })',
                   'db.netflix_userbase.deleteOne({"User_ID":2})',
                    'db.netflix_userbase.aggregate([{"$lookup": {"from": "netflix_userbase","localField": "User_ID","foreignField": "UserID","as": "joined"}}]);']

postgresql_queries = ["select User_ID,Join_Date,Country,Age from netflix_userbase where Subscription_Type= 'Basic'",
                      "INSERT INTO netflix_userbase(User_ID, Subscription_Type, Monthly_Revenue, Join_Date, Last_Payment_Date, Country, Age, Gender, Device, Plan_Duration) VALUES(2501, 'Basic', 18, '2022-08-31', '2023-07-21', 'United States', 33, 'Female', 'Smart TV', '1 Month') ON CONFLICT(User_ID) DO UPDATE SET Subscription_Type=EXCLUDED.Subscription_Type, Monthly_Revenue=EXCLUDED.Monthly_Revenue, Join_Date=EXCLUDED.Join_Date, Last_Payment_Date=EXCLUDED.Last_Payment_Date, Country=EXCLUDED.Country, Age=EXCLUDED.Age, Gender=EXCLUDED.Gender, Device=EXCLUDED.Device, Plan_Duration=EXCLUDED.Plan_Duration",
                      "UPDATE netflix_userbase SET Age = 30 WHERE User_ID = 1;",
                      "DELETE FROM netflix_userbase WHERE User_ID = 2;",
                      'SELECT a.Join_Date, b.Last_Payment_Date FROM netflix_userbase AS a LEFT JOIN netflix_userbase AS b ON a.User_ID = b.User_ID;']

couchbase_queries = ["select User_ID,Join_Date,Country,Age from netflix_userbase where Subscription_Type= 'Basic'",
                     'INSERT INTO netflix_userbase(KEY, VALUE) VALUES("2502",{"User_ID": "2502","Subscription_Type": "Basic","Monthly_Revenue": 18,"Join_Date": "2022-08-31","Last_Payment_Date": "2023-07-21","Country": "United States","Age": 33,"Gender": "Female","Device": "Smart TV","Plan_Duration": "1 Month"});',
                     "UPDATE netflix_userbase SET Age= 30 WHERE User_ID = 1",
                     "DELETE FROM netflix_userbase WHERE User_ID = 2;",
                      'SELECT a.Join_Date, b.Last_Payment_Date FROM netflix_userbase AS a LEFT JOIN netflix_userbase AS b ON a.User_ID = b.User_ID;']

# online retail

# mysql_queries = ['select ï»¿InvoiceNo, Description from online_retail where StockCode= "85123A"',
#                  "INSERT INTO online_retail (ï»¿InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country) VALUES ('8569I','33572','Big Car',3,'01-12-2010  08:26:00','234','17859','United Kingdom');",
#                  "UPDATE online_retail SET Country = 'Australia' WHERE ï»¿InvoiceNo = '536396';",
#                  "DELETE FROM online_retail WHERE ï»¿InvoiceNo = '536396';",
#                   'SELECT a.StockCode, b.Country FROM online_retail AS a LEFT JOIN online_retail AS b ON a.Quantity = b.Quantity where a.StockCode="85123";']
# 
# mongodb_queries = ['db.online_retail.find({"StockCode": "85123A"})',
#                    'db.online_retail.insertOne({ "ï»¿InvoiceNo": "8569I", "StockCode": "33572" , "Description": "Big Car", "Quantity": 3, "InvoiceDate": "01-12-2010  08:26:00" , "UnitPrice": "234", "CustomerID": "17859" , "Country": "United Kingdom"})',
#                    'db.online_retail.updateOne({"ï»¿InvoiceNo" :"536396"}, {"$set": {"Country":"Australia"} })',
#                    'db.online_retail.deleteOne({"ï»¿InvoiceNo" :"536396"})',
#                      'db.online_retail.aggregate([{"$lookup": {"from": "online_retail","localField": "Quantity","foreignField": "Quantity","as": "joined"}}]);']

# postgresql_queries = ["select ï»¿InvoiceNo, Description from online_retail where StockCode= '85123A'",
#                       "INSERT INTO online_retail (ï»¿InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country) VALUES ('8569I','33572','Big Car',3,'01-12-2010  08:26:00','234','17859','United Kingdom')",
#                       "UPDATE online_retail SET Country = 'Australia' WHERE ï»¿InvoiceNo = '536396';",
#                       "DELETE FROM online_retail WHERE ï»¿InvoiceNo = '536396';",
#                       "SELECT a.StockCode, b.Country FROM online_retail AS a LEFT JOIN online_retail AS b ON a.Quantity = b.Quantity where a.StockCode='85123';"]

# couchbase_queries = ["select ï»¿InvoiceNo, Description from online_retail where StockCode= '85123A'",
#                     'INSERT INTO online_retail(KEY, VALUE) VALUES("2502",{"ï»¿InvoiceNo": "8569I","StockCode": "33572","Description": "Big Car","Quantity": 3,"InvoiceDate": "01-12-2010  08:26:00","UnitPrice": "234","CustomerID": "17859","Country": "United Kingdom"});'
#                       "UPDATE online_retail SET Country = 'Australia' WHERE ï»¿InvoiceNo = '536396';",
#                       "DELETE FROM online_retail WHERE ï»¿InvoiceNo = '536396';",
#                       'SELECT a.StockCode, b.Country FROM online_retail AS a LEFT JOIN online_retail AS b ON a.Quantity = b.Quantity where a.StockCode="85123";']

# all_energy_statistics
# 
# mysql_queries = ['select country_or_area, commodity_transaction from all_energy_statistics where year= 1995',
#                  "INSERT INTO all_energy_statistics (country_or_area,commodity_transaction,year,unit,quantity,quantity_footnotes,category) VALUES ('India','Additives and Oxygenates - Exports',2000,'Metric tons,  thousand','10','1','additives_and_oxygenates');",
#                  "UPDATE all_energy_statistics SET country_or_area = 'Australia' WHERE year = 1997;",
#                  "DELETE FROM all_energy_statistics WHERE year = 1997;",
#                   "SELECT a.country_or_area, b.quantity FROM all_energy_statistics AS a LEFT JOIN all_energy_statistics AS b ON a.year = b.year where a.quantity='100' and a.country_or_area='France' and b.country_or_area='France';"]
# mongodb_queries = ['db.all_energy_statistics.find({"year": 1995})',
#                    'db.all_energy_statistics.insertOne({ "country_or_area": "India", "commodity_transaction": "Additives and Oxygenates - Exports" , "year": 2000, "unit": "Metric tons,  thousand", "quantity": "10" , "quantity_footnotes": "1", "category": "additives_and_oxygenates"})',
#                    'db.all_energy_statistics.updateOne({"year": 1997}, {"$set": {"country_or_area": "Australia"} })',
#                    'db.all_energy_statistics.deleteOne({"year": 1997})',
#                       'db.all_energy_statistics.aggregate([{"$lookup": {"from": "all_energy_statistics","localField": "year","foreignField": "year","as": "joined"}}]);']

# postgresql_queries = ["select country_or_area, commodity_transaction from all_energy_statistics where year= 1995",
#                  "INSERT INTO all_energy_statistics (country_or_area,commodity_transaction,year,unit,quantity,quantity_footnotes,category) VALUES ('India','Additives and Oxygenates - Exports',2000,'Metric tons,  thousand','10','1','additives_and_oxygenates');",
#                  "UPDATE all_energy_statistics SET country_or_area = 'Australia' WHERE year = 1997;",
#                  "DELETE FROM all_energy_statistics WHERE year = 1997;",
#                   "SELECT a.country_or_area, b.quantity FROM all_energy_statistics AS a LEFT JOIN all_energy_statistics AS b ON a.year = b.year where a.quantity='100' and a.country_or_area='France' and b.country_or_area='France';"]

# couchbase_queries = ["select country_or_area, commodity_transaction from all_energy_statistics where year= 1995",
#                     'INSERT INTO all_energy_statistics(KEY, VALUE) VALUES("2502",{"country_or_area": "India","commodity_transaction": "Additives and Oxygenates - Exports","year": 2000,"unit": "Metric tons,  thousand","quantity": "10","quantity_footnotes": "1","category": "additives_and_oxygenates"});'
#                  "UPDATE all_energy_statistics SET country_or_area = 'Australia' WHERE year = 1997;",
#                  "DELETE FROM all_energy_statistics WHERE year = 1997;",
#                   "SELECT a.country_or_area, b.quantity FROM all_energy_statistics AS a LEFT JOIN all_energy_statistics AS b ON a.year = b.year where a.quantity='100' and a.country_or_area='France' and b.country_or_area='France';"]

# spam

# mysql_queries = ["select * from spam;",
#                  "INSERT INTO spam (v1, v2) VALUES ('ham','Jungle');",
#                  "UPDATE spam SET v1 = 'spam' WHERE v2 = 'Lol your always so convincing.';",
#                  "DELETE FROM spam WHERE v2 = 'Lol your always so convincing.';"]
# mongodb_queries = ["db.spam.find()",
#                    'db.spam.insertOne({ "v1": "spam","v2":"Hello google"})',
#                    'db.spam.updateOne({"v2" :"Hello google"}, {"$set": {"v1":"ham"} })',
#                    'db.spam.deleteOne({"v2":"Anything"})']

# postgresql_queries = ["select * from spam;",
#                       "INSERT INTO spam (v1, v2) VALUES ('ham','Jungle');",
#                       "UPDATE spam SET v1 = 'spam' WHERE v2 = 'Lol your always so convincing.';",
#                       "DELETE FROM spam WHERE v2 = 'Lol your always so convincing.';"]

# couchbase_queries = ["select * from spam;",
#                      'INSERT INTO spam (KEY, VALUE) VALUES ("1",{"v1":"ham","v2":"Jungle"});',
#                      "UPDATE spam SET v1 = 'spam' WHERE v2 = 'Lol your always so convincing.';",
#                      "DELETE FROM spam WHERE v2 = 'Lol your always so convincing.';"]
