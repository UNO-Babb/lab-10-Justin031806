#MapPlot.py
#Name:
#Date:
#Assignment:



import coffee
import pandas
import matplotlib as plt

coffee=coffee.get_coffee()

#print(coffee[0]["Data"]["Scores"]["Total"])
years=[]
scores=[]
for bean in coffee:
    year=bean["Year"]
    score=bean["Data"]["Scores"]["Total"]
    if score !=0:
      years.append(year)
      scores.append(score)
    #print(year,score)

    df=pandas.DataFrame([{"Year":years,
                         "Score":scores}])
    
    print(df)
    df.plot(kind='scatter',x='Year',y='Score')
   
    plt.savefig("Output")


