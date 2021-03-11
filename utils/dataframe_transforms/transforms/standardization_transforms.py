# Standardizations

class StandardizationTransform():
    def __init__(self):
        pass

    def __call__(self, x):
        return self.transform(x)

    def transform(self, x):
        return x



class NullTransform(StandardizationTransform):
    def __init__(self):
        super().__init__()

    def transform(self, x):
        return super().transform(x)


class StringTransform(StandardizationTransform):
    def __init__(self):
        super().__init__()

    def transform(self, x):
        y = x.lower()
        return super().transform(y)


class SSNTransform(StandardizationTransform):
    def __init__(self):
        super().__init__()

    def transform(self, x):
        return super().transform(x)



# Transform Class Registry
#   Helps in dynamic composition of standardizer

transform_classes = {
    'ssid_pool': NullTransform,
    'student_id_pool': NullTransform,
    'ssn_pool': SSNTransform,
    'last_name_pool': StringTransform,
    'first_name_pool': StringTransform,
    'middle_name_pool': StringTransform,
    'gender_pool': NullTransform,
    'birth_date_pool': NullTransform,
    'guid': NullTransform,
}