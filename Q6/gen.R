library('DBI')
library('RSQLite')
png(file="out1_calgary_combined.jpg")

db = dbConnect(SQLite(), dbname="../311CallCentre.db")

query <- dbSendQuery(db, "SELECT 
        offered, 
        (answered*1.0)/offered*100 AS effectivness 
FROM 
        'calgary_combined' 
ORDER BY 
        offered;")
data <- dbFetch(query, n=-1)
print(data)
print(data$effectivness)
plot(
     y = data$effectivness,
     x = data$offered,
     type= 'p',
     ylab = "Effectiveness",
     xlab = "Received",
     main = "Effectiveness based as a function of calls received",
     col = "red")

dev.off()
