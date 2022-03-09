import pandas as pd
df = pd.read_csv(r"/Users/vipulkumar/Downloads/Contact Information (Responses) - Form Responses 1.csv")
print("Vipul Kumar,\n"
      "5/2,Ranjan Apartment,\n"
      "Bhatia Basti Main Road,\n"
      "Near ECC Flat,Kadma,\n"
      "Jamshedpur - 831005 \n"
      "Ph No: 8310073060")

for index, row in df.iterrows():
      print(f"{row['Name']}\n"
            f"{row['House/ Flat/ Block No.']},\n"
            f"{row['Apartment/ Road/ Area']},\n"
            f"{row['Landmark (Optional)']},\n"
            f"{row['City/ State']},\n"
            f"{row['Pin code']},\n"
            f"Ph No: {row['Phone number']}\n")
      input("Press enter for next address")