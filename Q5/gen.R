library('DBI')
library('RSQLite')
png(file="out1_calgary_combined.jpg")

db = dbConnect(SQLite(), dbname="../311CallCentre.db")

query <- dbSendQuery(db, "SELECT 
        STRFTIME('%m', date) AS date, 
        AVG(offered) AS received 
FROM 
        'calgary_combined' 
GROUP BY 
        STRFTIME('%m', date);")
data <- dbFetch(query, n=-1)

barplot(height = data$received,
        xlab = "months",
        ylab = "received",
        main = "Peak Months1",
        names.arg = as.character(data$date),
        col = rainbow(length(data$date)))

dev.off()
