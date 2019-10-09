library('chemometrics')
data <- read.table("auto-mpg.data")
colnames(data) <- c("mpg" , "cyclinders" , "displacement" , "horsepower" , "weight" , "acceleration" , "model.year" , "origin" , "car.name")
summary(data)
m <- lm(cbind(data$mpg,data$acceleration,data$horsepower) ~ data$cyclinders + data$displacement + data$weight + data$model.year)
summary(m)
mm <- manova(m)
summary(mm)
data$car.name <- NULL
data$horsepower[data$horsepower=='?'] <- NA
data$horsepower<- as.numeric(data$horsepower)
cor(data)
cov(data)