class Fuzificare:
    def fuzificareTrapez(self, x, multime):
        return max(0,
                   min((x - multime[0]) / (multime[1] - multime[0]), 1, (multime[3] - x) / (multime[3] - multime[2])))

    def fuzificareTriunghi(self, x, multime):
        if len(multime) == 3:
            return max(0,
                       min((x - multime[0]) / (multime[1] - multime[0]), 1,
                           (multime[2] - x) / (multime[2] - multime[1])))
        return max(0.0, float(((-1) * x / (multime[1] - multime[0]) + 1)), float(x / (multime[1] - multime[0]) - 1))

    def fuzificareTemperatura(self, x, multime, cold, veryHot, firstCommon, lastCommon):
        if x < firstCommon and multime == cold:
            return 1.0
        elif x > lastCommon and multime == veryHot:
            return 1.0
        elif len(multime) == 3 or len(multime) == 2:
            return self.fuzificareTriunghi(x, multime)
        return self.fuzificareTrapez(x, multime)

    def fuzificareCapacitate(self, x, multime):
        if len(multime) == 3 or len(multime) == 2:
            return self.fuzificareTriunghi(x, multime)
        return self.fuzificareTrapez(x, multime)

    def fuzificarePutere(self, x, multime):
        if len(multime) == 3 or len(multime) == 2:
            return self.fuzificareTriunghi(x, multime)
        return self.fuzificareTrapez(x, multime)
