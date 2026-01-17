# 1️⃣ Without parameter, without return
def no_pr():
    print("Without parameter, without return")

no_pr()

print()


# 2️⃣ With parameter, without return
def with_param_no_return(message):
    print(message)

with_param_no_return("With parameter, without return")

print()


# 3️⃣ Without parameter, with return
def no_param_with_return():
    return "Without parameter, with return"

print(no_param_with_return())

print()


# 4️⃣ With parameter, with return
def with_param_with_return(a, b):
    return a + b

print(f"With parameter, with return >>> {with_param_with_return(2, 2)}")

