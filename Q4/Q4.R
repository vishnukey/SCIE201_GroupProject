library('DBI')
library('RSQLite')
png(file="out1_calgary_combined.jpg")

db = dbConnect(SQLite(), dbname="../311CallCentre.db")

query <- dbSendQuery(db, "SELECT 
        STRFTIME('%Y-%m', date) AS date, 
        AVG(answered)/AVG(offered)*100 AS effectiveness 
FROM 
        'calgary_combined' 
GROUP BY 
        STRFTIME('%Y-%m', date);")
data <- dbFetch(query, n=-1)

barplot(height = data$effectiveness,
        xlab = "months",
        ylab = "effectiveness",
        main = "Effectiveness by month",
        names.arg = as.character(data$date),
        col = rainbow(length(data$date)))

dev.off()
