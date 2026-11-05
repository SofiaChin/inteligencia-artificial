import yaml
import re

class MotorInferencia:
    def __init__(self, ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = yaml.safe_load(archivo)
        self.base_hechos = datos.get('facts', [])
        self.base_reglas = datos.get('rules', [])

    def _unificar(self, atomo_var, atomo_gr):
        m1 = re.match(r"(\w+)\(([^)]+)\)", atomo_var)
        m2 = re.match(r"(\w+)\(([^)]+)\)", atomo_gr)
        if not m1 or not m2 or m1.group(1) != m2.group(1): return None
        args1 = [a.strip() for a in m1.group(2).split(',')]
        args2 = [a.strip() for a in m2.group(2).split(',')]
        if len(args1) != len(args2): return None
        sub = {}
        for a1, a2 in zip(args1, args2):
            if a1.islower():
                if a1 in sub and sub[a1] != a2: return None
                sub[a1] = a2
            elif a1 != a2: return None
        return sub

    def _sustituir(self, atomo, sub):
        m = re.match(r"(\w+)\(([^)]+)\)", atomo)
        args = [a.strip() for a in m.group(2).split(',')]
        return f"{m.group(1)}({','.join([sub.get(a, a) for a in args])})"

    def _eval_conds(self, conds, hechos, sub, idx, salidas):
        if idx == len(conds):
            salidas.append(sub.copy())
            return
        actual = self._sustituir(conds[idx], sub)
        for f in hechos:
            s = self._unificar(actual, f)
            if s is not None:
                nueva_s = {**sub, **s}
                self._eval_conds(conds, hechos, nueva_s, idx + 1, salidas)

    def forward_chain(self):
        db = list(self.base_hechos)
        injeridos = []
        while True:
            nuevos = []
            for r in self.base_reglas:
                salidas = []
                self._eval_conds(r['if'], db, {}, 0, salidas)
                for sub in salidas:
                    concl = self._sustituir(r['then'], sub)
                    if concl not in db and concl not in nuevos:
                        nuevos.append(concl)
                        injeridos.append(concl)
            if not nuevos: break
            db.extend(nuevos)
        return db, injeridos

    def backward_chain(self, meta, visitados=None):
        if visitados is None: visitados = set()
        if meta in self.base_hechos: return True, [f"Hecho encontrado: {meta}"]
        if meta in visitados: return False, [f"Loop cortado: {meta}"]
        camino = [f"Objetivo actual: {meta}"]
        for r in self.base_reglas:
            sub = self._unificar(r['then'], meta)
            if sub is not None:
                camino.append(f"Aplica regla {r['id']}")
                exito = True
                sub_camino = []
                for cond in r['if']:
                    c_sub = self._sustituir(cond, sub)
                    res, p = self.backward_chain(c_sub, visitados | {meta})
                    sub_camino.extend(p)
                    if not res:
                        exito = False
                        break
                if exito:
                    return True, camino + sub_camino + [f"Validado: {meta}"]
                camino.extend(sub_camino)
        return False, camino + [f"Descartado: {meta}"]

if __name__ == '__main__':
    motor = MotorInferencia('kb.yaml')
    print("=== RESOLUCION FORWARD CHAINING ===")
    hechos_finales, orden = motor.forward_chain()
    print("Secuencia de inferencia:", orden)
    for target in ["AccesoNoche(Ana)", "AccesoNoche(Luis)", "AccesoNoche(Marta)"]:
        print(f"[{target}] -> {'SI' if target in hechos_finales else 'NO'}")

    print("\n=== RESOLUCION BACKWARD CHAINING ===")
    for target in ["AccesoNoche(Ana)", "AccesoNoche(Luis)", "AccesoNoche(Marta)"]:
        status, trace = motor.backward_chain(target)
        print(f"\n[{target}] -> {'SI' if status else 'NO'}")
        for step in trace: print("  *", step)
