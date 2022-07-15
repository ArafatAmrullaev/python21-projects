class Cars:
    objects = []
    _id = 0
    type_kuz = ['седан', 'универсал. купе', 'хэтчбек', 'минивен', 'внедорожник', 'пикап']
    def __init__(self, mark, model, year, volume, color, type_, prob, price):
        self.mark = mark
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.prob = prob
        self.price = price
        if type_ in Cars.type_kuz:
            self.type_ = type_
        else:
            raise Exception('Выберите правильный тип!')
        Cars.objects.append(self)

        Cars._id += 1

    # def __str__(self):
    #     return f'vzs'
    
