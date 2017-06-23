import fileinput

def return_value(text):
     # split the text
    words = text.split()

    count = 1
    # for each word in the line:
    for word in words:
        if (count != 2):
            count += 1
            continue
        else:
            return word


# Read file and save fitted potential values as variables
for line in fileinput.input():
    if "A\t" in line:
       	var_A = return_value(line)
    elif "B\t" in line:
        var_B = return_value(line)
    elif "lambda\t" in line:
        var_lambda = return_value(line)
    elif "mu\t" in line:
        var_mu = return_value(line)
    elif "gamma\t" in line:
        var_gamma = return_value(line)
    elif "n\t" in line:
        var_n = return_value(line)
    elif "c\t" in line:
        var_c = return_value(line)
    elif "d\t" in line:
        var_d = return_value(line)
    elif "h\t" in line:
        var_h = return_value(line)
    elif "S\t" in line:
        var_S = float(return_value(line)) # M must be either 1.0 or 3.0
        if (var_S != 1.0) or (var_S != 3.0):
            var_S = str(3.0)
    elif "R\t" in line:
        var_R = float(return_value(line))

s = " "

print("# This is the Si parameterization from a particular Tersoff paper:")
print("# J. Tersoff, Phys Rev B, 39, 5566-5568 (1989)")
print("# and errata (PRB 41, 3248)")

print("# format of a single entry (one or more lines):")
print("#   element 1, element 2, element 3,")
print("#   m, gamma, lambda3, c, d, costheta0, n, beta, lambda2, B, R, D, lambda1, A\n\n")

print("Si  Si   Si\n"+var_S+" 1.0 "+"0.0 "+var_c+s+var_d+s+var_h+"\n"+s+var_n+s+var_gamma+s+var_mu+s+var_B+s+str(var_R-0.15)+" 0.15 "+var_lambda+s+var_A)


# Original SiC.tersoff values:
# Si  Si  Si  3.0 1.0 0.0  100390  16.217   -.59825 .78734
#           0.0000011     1.73222  471.18  2.85   0.15    2.4799  1830.8
