# Project 1
import pprint
import pandas as pd
import random 
from math import sqrt



POINT=tuple[float, float, float]

class Point:
    def __init__ (self, p1: POINT, p2: POINT) -> float:
        self.p1=p1
        self.p2=p2
        
    def __repr__(self):
        return f'Point1: {self.p1[0]} as x, {self.p1[1]} as y, and {self.p1[2]} as z. Point2: {self.p2[0]} as x, {self.p2[1]} as y, and {self.p2[2]} as z.'

# calculate Euclidean distance
    def distance (self, point1: POINT, point2: POINT) -> float:
        distance_result= sqrt ((self.p2[0]-self.p1[0])**2 + (self.p2[1]-self.p1[1])**2 + (self.p2[2]-self.p1[2])**2)
        return distance_result

# Initiate centers
    def initiate_centers (self):
        k=int(input('Please Enter K as the numbers of clustering: '))
        centers=[(random.randint(-10,10), random.randint(-10, 10), random.randint(-10, 10)) for _ in range(k)]
        return centers
    
#calculate K_means
    def k_means (self, points):
        
        centers= Point.initiate_centers(self)
        print(centers)
        result = [
            {
                "center": c,
                "points": [],
            }
            for c in centers]
        
        for p in points:
            index, minimum = 0, Point.distance (self, p, centers[0])
            
            i = 1
            #for i, center in enumerate(centers):
            while i < len(centers):
                d = Point.distance(self, p, centers[i])
                if d < minimum:
                     index, minimum = i, d

                i += 1

            result[index]["points"].append(p)
        
        return result

    
    def update_cluster (self):
        
        while True:
            clusters = Point.k_means(self, points)
            new_centers = []
            for i in clusters:
                x, y, z = zip(*i["points"])
                new_centers.append(
                    (
                        sum(x) / len(x),
                        sum(y) / len(y),
                        sum(z) / len(z),
                    )
                )

            if new_centers == centers:
                break

            centers = new_centers
            
        pprint.pprint(clusters)

    

df= pd.read_csv("/Users/mahlagha/Desktop/Works in Progress/Data Science/Daneshkar/1- Python/points.csv", na_values=['?'])
df.dropna(inplace= True)
 
# Turning dataframe into a list
points_list= list(df.itertuples(index=False, name=None))
#print(points)

if __name__ == "__main__":
    n = int(input("Enter the number of data points: "))
    samples=[]
    for i in range(n):
        samples.append(random.choice(points_list))
    print(samples)
    print()
    
    
    obj1= Point(samples[0], samples[1])
    print(obj1)
    print()
    print(obj1.distance(samples[0], samples[1]))
    print()
    print(obj1. k_means(points_list))
    print()
    print(obj1.update_cluster())
