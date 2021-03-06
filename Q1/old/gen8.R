library('DBI')
library('RSQLite')
png(file="out8_city_script.jpg")

db = dbConnect(SQLite(), dbname="../311CallCentre.db")

query <- dbSendQuery(db, "SELECT date, offered, (answered*1.0)/offered*100 AS effectiveness FROM 'city_script' WHERE STRFTIME('%Y',date) = '2015' AND (answered*1.0)/offered*100 < 100 ORDER BY date;")
data <- dbFetch(query, n=-1)
plot(
     y = data$effectiveness,
     x = c(1:length(data$date)),
     type= 'b',
     ylab = "effectiveness",
     xlab = "date",
     main = "Effectivness over time for city_script",
     col = "blue")

print(data)
dev.off()
