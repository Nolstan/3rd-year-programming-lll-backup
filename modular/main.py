# import mathpackage.stats as stats
# import mathpackage.geom as geom

# IMPORTING FROM A SUB FOLDER
import mathpackage.subpackage.stats as stats
import mathpackage.subpackage.geom as geom


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(f'Minimum = { stats.min_(nums)}') 
    print(f'Maximum = { stats.max_(nums)}')


    print(f"Area of circle with radius 5 is {geom.circle(5).area():.2f}")




