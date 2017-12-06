library('DBI')
library('RSQLite')
png(file="out1_calgary_combined.jpg")

db = dbConnect(SQLite(), dbname="../311CallCentre.db")

query <- dbSendQuery(db, "SELECT 
        AVG(offered), 
        AVG(answered)/AVG(offered)*100 AS answered, 
        AVG(abandonned)/AVG(offered)*100 AS abandoned 
FROM 
        'calgary_combined';")

data <- dbFetch(query, n=-1)

print(data)
items <- c(data$answered, data$abandoned)
print(items)
cols <- c("red", "blue")

pie(items,
        labels = paste(as.character(round(items, 2)), "%"),
        radius = 1,
        main = "Number of calls answered vs numbered abandoned",
        col = cols
)

legend(
        "bottomright",
        c("answered", "abandoned"),
        cex = 0.8,
        fill = cols
)
dev.off()
