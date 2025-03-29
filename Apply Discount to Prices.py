def discount_prices(sentence: str, discount: int) -> str:
    # self.discount = discount/100
    word_list = sentence.split(" ")
    new_str = ""
    for i in range(len(word_list)):
        word = word_list[i]
        price = word[1:]
        substr = word
        if word[0] == "$" and price.isdigit():
            price = int(price)
            discounted_price = "{:.2f}".format(price - (price * (discount/100)))
            substr = f"${discounted_price}"
        if i == len(word_list) - 1:
            new_str += f"{substr}"
        else:
            new_str += f"{substr} "
    return new_str

print(discount_prices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100))