iris<-read.csv("/Users/will/Documents/DMWebApp/home_site/data_mining/a.csv")

args<-commandArgs(TRUE)

i<-as.numeric(1)
j<-as.numeric(2)
cluster<-as.numeric(3);

selectedData <- iris[, c(i,j)]

clusters<-kmeans(selectedData,cluster)

par(mar = c(5.1, 4.1, 0, 1))

jpeg('/Users/will/Documents/DMWebApp/home_site/data_mining/plot.jpg')
plot(selectedData,
     col = clusters$cluster,
     pch = 20, cex = 3)
points(clusters$centers, pch = 4, cex = 4, lwd = 4)
dev.off()
