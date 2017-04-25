library(devtools)
dev_mode(on=T)
install_github("sgrieve/pgirmess")
data = read.csv("Data/Mid_Data_Final.csv")
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/Mid_Data_Final_veg_curv.csv")
xy = data.frame(data$X,data$Y)
plot(xy)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran")
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran")
print(pgi.cor)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran")
plot(pgi.cor)
print(pgi.cor)
plot(pgi.cor)
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran")
plot(pgi.cor)
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=250)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=251)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=100)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbclass=5, nbins=100)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
install_github("sgrieve/pgirmess")
library(pgirmess)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/Mid_Data_Final_veg_curv.csv")
xy = data.frame(data$X,data$Y)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
breaks
breaks1<-seq(1,10,l=20)
break1
breaks1
breaks1[1]
breaks1[0]
breaks1[2]
breaks1[:5]
breaks1[1:5]
breaks1[1:10]
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
coords<-as.matrix(xy)
matdist<-dist(coords)
etendue<-range(matdist)
etendue
matdist
breaks1<-seq(etendue[1],etendue[2],l=700)
breaks2<-breaks1+0.000001
breaks<-cbind(breaks1[1:length(breaks1)-1],breaks2[2:length(breaks2)])
breaks
breaks[1,1]
cbind(dist.class = rowMeans(breaks), coef = mat[, 1], p.value
breaks[1,1] <- breaks[1,1] - 1e-6
breaks[1,1]
breaks[1,250]
breaks[250,1]
breaks[250,3]
breaks[250,2]
breaks[1:250,2]
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
print(pgi.cor)
plot(pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=200)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=260)
plot(pgi.cor)
write.csv(file="tmp.csv", x=pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=700)
write.csv(file="tmp.csv", x=pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=300)
write.csv(file="tmp.csv", x=pgi.cor)
plot(pgi.cor)
plot(pgi.cor)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/esc_area_autocorr.csv")
xy = data.frame(data$X,data$Y)
xy = data.frame(data$X,data$Y)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/Escarpment_Data_Width.csv")
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/Escarpment_Data_width.csv")
xy = data.frame(data$X,data$Y)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=300)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=100)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=50)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=10)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/Mid_Data_Final_veg_curv.csv")
xy = data.frame(data$X,data$Y)
pgi.cor <- correlog(coords=xy,z=data$Area, method="Moran", nbins=300)
write.csv(file="tmp.csv", x=pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$width, method="Moran", nbins=300)
write.csv(file="width_ac.csv", x=pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$Length, method="Moran", nbins=300)
write.csv(file="length_ac.csv", x=pgi.cor)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/esc_areas.csv")
xy = data.frame(data$x,data$y)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=300)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=251)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=700)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=554])
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=554)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=250)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=251)
pgi.cor <- correlog(coords=xy,z=data$Non_Escarpment_Hollows_area, method="Moran", nbins=2000)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/esc_areas.csv")
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300)
plot(pgi.cor)
write.csv(file="esc_area_ac.csv", x=pgi.cor)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/non_esc_areas.csv")
xy = data.frame(data$x,data$y)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300)
plot(pgi.cor)
write.csv(file="non_esc_area_ac.csv", x=pgi.cor)
q()
install_github("sgrieve/pgirmess")
library(devtools)
dev_mode(on=T)
install_github("sgrieve/pgirmess")
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300)
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=300, limit=60)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=100, limit=60)
install_github("sgrieve/pgirmess")
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=100, limit=60)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=60, limit=60)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=61, limit=60)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=41, limit=40)
plot(pgi.cor)
write.csv(file="non_esc_area_ac_small.csv", x=pgi.cor)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/esc_areas.csv")
xy = data.frame(data$x,data$y)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=41, limit=40)
plot(pgi.cor)
write.csv(file="esc_area_ac_small.csv", x=pgi.cor)
install_github("sgrieve/pgirmess")
library(pgirmess)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=41, limit=40)
plot(pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=81, limit=80)
plot(pgi.cor)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=61, limit=60)
plot(pgi.cor)
write.csv(file="esc_area_ac_small.csv", x=pgi.cor)
data = read.csv("/home/sgrieve/Hollow_Paper_Plotting/Data/non_esc_areas.csv")
xy = data.frame(data$x,data$y)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=61, limit=60)
pgi.cor <- correlog(coords=xy,z=data$area, method="Moran", nbins=61, limit=60)
plot(pgi.cor)
q()
