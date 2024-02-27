current_package_weight = 0
sent_package_weight = 0
sent_package_number = 0
total_package_weight_sent = 0
unused_space_capacity = 0
unused_capacity= []

number_of_items = input("How many items do you want to ship please?   ")
if number_of_items.isdigit():
    number_of_items = int(number_of_items)

    for item in range (number_of_items): 
        item_weight = input("\nenter item weight please:>>>>>>>    ")
        item_weight = int(item_weight)

        current_package_weight += item_weight

        if item_weight == 0:
            print("Terminating the program, good bye!! ")
            break
        elif item_weight < 0 or item_weight > 10 :
            print(f"ERROR!!! you entered {item_weight} \nweight of item added must be between {1} and {10} inclusive>>> ") 
            break
        elif item_weight >=1 or item_weight <=10 :

            if current_package_weight > 20 :      
                sent_package_weight = current_package_weight - item_weight
                sent_package_number +=1
                total_package_weight_sent += sent_package_weight
                current_package_weight = item_weight
                print(f"\npackage number {sent_package_number} has {sent_package_weight} KG in it, it's now being sent\n\n")
                unused_space_capacity = 20 - sent_package_weight
                print (f"unused space capacity for package number '{sent_package_number}' is {unused_space_capacity} KG\n\nLoading the next package now\n")
                unused_capacity.append(unused_space_capacity)
                unused_space_capacity = 0
            
            elif current_package_weight == 20:
                sent_package_weight=current_package_weight
                total_package_weight_sent += sent_package_weight
                sent_package_number += 1
                current_package_weight = 0
                unused_space_capacity = 20 - sent_package_weight
                print (f"unused space capacity for package number '{sent_package_number}' is {unused_space_capacity} KG\n")
                unused_capacity.append(unused_space_capacity)
                unused_space_capacity = 0
      
    if current_package_weight > 0:
        sent_package_number += 1
        sent_package_weight = current_package_weight
        total_package_weight_sent +=sent_package_weight
        print(f"\npackage number {sent_package_number} has {sent_package_weight} KG in it, it's now being sent\n\n")
        unused_space_capacity = 20 - sent_package_weight
        print (f"unused space capacity for package number '{sent_package_number}' is {unused_space_capacity} KG\n\nLoading the next package now\n")
        unused_capacity.append(unused_space_capacity)
        print("----------------------------------- \n"* 3)
        print("\nlooks like no more items being loaded ")
        print("\n\t  In Summary\n\n")

    #print(unused_capacity) # printing the list of unsed capacity per package respectively
    #print(len(unused_capacity))
    for i in unused_capacity:
        
        if all(item == unused_capacity[0] for item in unused_capacity):
           print("All packages have the same unused capacity\n")
           break
        else:
            package_with_max_unused_capacity = max(unused_capacity)

            package_with_max_unused_capacity = unused_capacity.index(max(unused_capacity))
            print(f"The package with the maximum Unused Capacity is Package number '{package_with_max_unused_capacity + 1}'\n")
            break
        
    print(f"Total Weight of all sent Packages is {total_package_weight_sent} KG\n")
    print(f"Total number of Packages sent is {sent_package_number} Package(s)\n")
    #print(f"The package with the maximum Unused Capacity is Package number '{package_with_max_unused_capacity + 1}'\n")
    unused_capacity = (sent_package_number * 20 ) - total_package_weight_sent
    print(f"Total Unused Capacity ia {unused_capacity} KG\n")


else:
    print("Error!! enter a valid number please")

                      