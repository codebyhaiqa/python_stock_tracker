Stock_list={
    "AAPL":211.16,
    "MSFT":503.32,
    "GOOGL":180.19,
    "AMZN":225.02,
    "TSLA":313.51,
    "NVDA":164.92,
    "META":717.51,
    "BRK.B":475.86,
    "JNJ":156.90,
    "JPM":286.86,
}
print("\nWelcome to the stock portfolio tracker")
print("Type 'DONE' to Finish")
while True:
     Stock_name=input("\nEnter the name of the stock:").upper()
     if Stock_name == 'DONE':
         print("✅ Exiting the tracker.Thanks for using.")
         break
     quantity=int(input("Enter the number of shares you own:"))
     if quantity < 0:
         print("❌ Quantity cannot be negative\n")
         continue
     if Stock_name in Stock_list:
        print("\nStock Name:",Stock_name)
        print("Your Stock Quantity:",quantity)
        print("Current Price:",Stock_list[Stock_name])
        total=quantity*Stock_list[Stock_name]
        print("Total investment : $",total)
     else:
        print("❌",Stock_name,"is not available")
     retry=input("\nDo you want to invest in another company? (y/DONE): ").upper()
     if retry == 'y'or retry =='Y':
          continue
     elif retry=='DONE':
           print("✅ Exiting the tracker.Thanks for using.")
           break
     else:
         print("⚠️ Invalid choice.")