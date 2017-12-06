library('DBI')
library('RSQLite')
png(file="out1_calgary_combined.jpg")

db = dbConnect(SQLite(), dbname="../311CallCentre.db")

query <- dbSendQuery(db, "SELECT offered, avg_ans_delay_seconds FROM 'calgary_combined';")
data <- dbFetch(query, n=-1)
plot(
     y = data$avg_ans_delay_seconds,
     x = data$offered,
     type= 'p',
     ylab = "Average Delay (seconds)",
     xlab = "Calls Received",
     main = "Delay as a fucntion of Calls Received\n for calgary_combined",
     col = "blue")

print(data)
dev.off()
