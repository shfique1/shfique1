import pandas as pd
first_page=pd.read_csv('scraped_products1.csv')
second_page=pd.read_csv('scraped_products2.csv')
third_page=pd.read_csv('scraped_products3.csv')
four_page=pd.read_csv('scraped_products4.csv')
five_page=pd.read_csv('scraped_products5.csv')
six_page=pd.read_csv('scraped_products6.csv')
seven_page=pd.read_csv('scraped_products7.csv')
eight_page=pd.read_csv('scraped_products8.csv')
nine_page=pd.read_csv('scraped_products9.csv')
ten_page=pd.read_csv('scraped_products10.csv')
eleven_page=pd.read_csv('scraped_products11.csv')
twelth_page=pd.read_csv('scraped_products12.csv')
thirteen_page=pd.read_csv('scraped_products13.csv')
fourteen_page=pd.read_csv('scraped_products14.csv')
fifteen_page=pd.read_csv('scraped_products15.csv')
sixteen_page=pd.read_csv('scraped_products16.csv')
Seventeen_page=pd.read_csv('scraped_products17.csv')
Eighteen_page=pd.read_csv('scraped_products18.csv')
NineTeen_page=pd.read_csv('scraped_products19.csv')
Twentiath_page=pd.read_csv('scraped_products20.csv')
TwentyOne_page=pd.read_csv('scraped_products21.csv')
TwentyTwo_page=pd.read_csv('scraped_products22.csv')
TwentyThree_page=pd.read_csv('scraped_products23.csv')
TwentyFour_page=pd.read_csv('scraped_products24.csv')
TwentyFive_page=pd.read_csv('scraped_products25.csv')



combined_data=pd.concat([first_page,second_page,third_page,four_page,five_page,six_page,seven_page,eight_page,nine_page,ten_page,eleven_page,twelth_page,thirteen_page,fourteen_page,fifteen_page,sixteen_page,Seventeen_page,Eighteen_page,NineTeen_page,Twentiath_page,TwentyOne_page,TwentyTwo_page,TwentyThree_page,TwentyFour_page,TwentyFive_page],ignore_index=True)

print("number of products scraped is : ",len(combined_data))
combined_data.to_csv('Jcpenney_Men_Data.csv', index=False)