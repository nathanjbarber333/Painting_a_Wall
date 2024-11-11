#step 1(calculating wall area)
wall_height=int(input())
wall_width=int(input())
wall_area=(wall_height)*(wall_width)
print(f"Wall area: {wall_area:.1f} sq ft")

#step 2(calculating paint needed)
paint_can_cost=float(input())
paint_needed=(wall_area)/350
print(f"Paint needed: {paint_needed:.3f} gallons")

#step 3(number of 1 gallon cans)
import math
num_gal_cans=math.ceil(paint_needed)
print(f"Cans needed: {num_gal_cans} can")

#step 4(calculating paint cost, tax, and total cost)
print(f"Paint cost: ${paint_can_cost: .2f}")
sales_tax=(paint_can_cost)*.07
print(f"Sales tax: ${sales_tax: .2f}")
total_cost=(paint_can_cost)+(sales_tax)
print(f"Total cost: ${total_cost: .2f}")