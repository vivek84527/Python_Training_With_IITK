def show(empName, phone="1234567890", city="Lucknow", company="XYZ"):
    print("\nempName=",
          empName,
          "phone=", phone,
          "city=", city,
          "company= ", company)


# Rule-1

show("Chintu")

# Rule-2


show("Pappu", "999888")  # 2 Positional Arguments

# Rule-3


show(empName="Pappu", phone="877666")  # Keyword Argument
show(phone="877666", empName="Pappu")
show(empName="Pappu", city="Kanpur")

# Rule-4

show("Alisha", "9898", city="Delhi")  # Mixed mode

# following calls would be invalid:
# ---------------------------------------
# show()                          # required argument missing
# show(empName="Jeetendra", '99998888')  # non-keyword argument after a keyword argument
# show("Jeetendra", empName="Alisha")    # duplicate value for the same argument
# show(name="Alisha" )                   # unknown keyword argument
