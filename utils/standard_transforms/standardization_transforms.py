# Standardizations

class StandardizationTransform():
    def __init__(self):
        pass

    def __call__(self, x):
        return self.transform(x)

    def transform(self, x):
        return x


class StringTransform(StandardizationTransform):
    def __init__(self):
        super().__init__()

    def transform(self, x):
        y = x.lower().strip()
        return super().transform(y)


class NullTransform(StandardizationTransform):
    def __init__(self):
        super().__init__()

    def transform(self, x):
        return super().transform(x)


## Specifc Transformation Classes ##


class FirstNameTransform(StringTransform):
    def __init__(self):
        super().__init__()
        self._field = 'first_name_pool'

    def transform(self, x):
        if type(x) == dict:
            x[self._field] = super().transform(x[self._field])
        else:
            raise NotImplementedError(f"{type(x)} not supported for {self._field}")
        return x


class LastNameTransform(StringTransform):
    def __init__(self):
        super().__init__()
        self._field = 'last_name_pool'

    def transform(self, x):
        if type(x) == dict:
            x[self._field] = super().transform(x[self._field])
        else:
            raise NotImplementedError(f"{type(x)} not supported for {self._field}")
        return x


class MiddleNameTransform(StringTransform):
    def __init__(self):
        super().__init__()
        self._field = 'middle_name_pool'

    def transform(self, x):
        if type(x) == dict:
            x[self._field] = super().transform(x[self._field])
        else:
            raise NotImplementedError(f"{type(x)} not supported for {self._field}")
        return x


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
    'last_name_pool': LastNameTransform,
    'first_name_pool': FirstNameTransform,
    'middle_name_pool': MiddleNameTransform,
    'gender_pool': NullTransform,
    'birth_date_pool': NullTransform,
    'guid': NullTransform,
}