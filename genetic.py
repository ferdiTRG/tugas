import random 
from staticdata import courses_data, rooms_data, timeslots_data 
from generator import angkatan25, angkatan24, angkatan23 
from datatyp import courseclass

class Schedule: 
 def __init__(self, course_classes, rooms, timeslots): 
    self.course_classes = course_classes 
    self.rooms = rooms 
    self.timeslots = timeslots 
    self.assignments = {} 

 def randomize(self): 
    for cclass in self.course_classes: 
        valid_pairs = [(room, ts) for room in self.rooms for ts in self.timeslots if 
ts.slot_id in room.waktu_tersedia] 
        self.assignments[cclass] = random.choice(valid_pairs) 

 def fitness(self, muridd): 
    penalty = 0 

    room_usage = {} 
    dosen_usage = {} 
    murid_usage = {} 

    for cclass, (room, ts) in self.assignments.items(): 

        # Ketersediaan ruangan 
        if ts.slot_id not in room.waktu_tersedia: 
            penalty += 100_000 

        # Konflik ruangan 
        key_room = (room, ts) 
        if key_room in room_usage: 
            penalty += 100_000 
        else: 
            room_usage[key_room] = cclass 

        # Konflik dosen 
        key_dosen = (cclass.dosen, ts) 
        if key_dosen in dosen_usage: 
            penalty += 100_000 
        else: 
            dosen_usage[key_dosen] = cclass 
 
        over = len(cclass.muridd) - room.kapasitas 
        if over > 30:  
            penalty += over-30  

# Konflik mahasiswa 
    for murid in muridd: 
        taken = {} 
        for cclass in self.course_classes: 
            if cclass.course.nama in murid.courses and murid in cclass.muridd: 
                room, ts = self.assignments[cclass] 
                if ts in taken: 
                    penalty += 100_000 
                else: 
                    taken[ts] = cclass 

    return penalty

#Algoritma Genetika 
def crossover(p1, p2): 
    child = Schedule(p1.course_classes, p1.rooms, p1.timeslots) 
    child.assignments = {} 
    for cclass in p1.course_classes: 
        if random.random() < 0.5: 
            child.assignments[cclass] = p1.assignments[cclass] 
        else: 
            child.assignments[cclass] = p2.assignments[cclass] 
    return child 

def mutate(schedule): 
    cclass = random.choice(schedule.course_classes) 
    valid_pairs = [(room, ts) for room in schedule.rooms for ts in 
schedule.timeslots if ts.slot_id in room.waktu_tersedia] 
    schedule.assignments[cclass] = random.choice(valid_pairs) 

def assign_dosens_to_sections(courses): 
    """Assign dosen to course sections using round-robin or random assignment"""
    course_classes = [] 

    for course in courses: 
        available_dosen = course.dosen.copy() 

        for i in range(course.jumlah_class): 
            section_letter = chr(65 + i) 
            dosen = available_dosen[i % len(available_dosen)] 

            course_class = courseclass(course, section_letter, dosen) 
            course_classes.append(course_class) 

    return course_classes 

def genetic_algorithm(courses, rooms, timeslots, muridd, population_size=50, 
                    generations=100): 
    course_classes = assign_dosens_to_sections(courses) 

    for murid in muridd: 
        for cnama in murid.courses: 
            selected_classes = [c for c in course_classes if c.course.nama == cnama] 
            target = min(selected_classes, key=lambda x: len(x.muridd)) 
            target.muridd.append(murid) 

    population = [] 
    for _ in range(population_size): 
        s = Schedule(course_classes, rooms, timeslots) 
        s.randomize() 
        population.append(s) 

    for gen in range(generations): 
        scored = [(s.fitness(muridd), s) for s in population] 
        scored.sort(key=lambda x: x[0]) 
        best_score, best_schedule = scored[0] 
        print(f"Gen {gen} best fitness = {best_score}") 

        if best_score == 0: 
            return best_schedule 

        survivors = [s for _, s in scored[:population_size//2]] 
        children = [] 
        while len(children) < population_size//2: 
            p1, p2 = random.sample(survivors, 2) 
            child = crossover(p1, p2) 
            if random.random() < 0.5:  
                mutate(child) 
            children.append(child) 

        population = survivors + children 

    return scored[0][1] 


if __name__ == "__main__":

    muridd = angkatan24() + angkatan23() + angkatan25() 

best = genetic_algorithm(courses_data, rooms_data, timeslots_data, muridd, 
                            population_size=1000, 
                            generations=100) 

print("\n=== Jadwal Terbaik ===") 
for cclass, (room, ts) in best.assignments.items(): 
    murid_count = len(cclass.muridd) 
    print(f"{cclass} -> {room.nama} di {ts} ({murid_count} mahasiswa)") 

print("\n=== Jadwal dosen ===") 
dosen_schedule = {} 
for cclass, (room, ts) in best.assignments.items(): 
    if cclass.dosen not in dosen_schedule: 
        dosen_schedule[cclass.dosen] = [] 
    dosen_schedule[cclass.dosen].append((cclass, room, ts)) 

for dosen, assignments in dosen_schedule.items(): 
    print(f"\n{dosen}:") 
    for cclass, room, ts in assignments: 
        print(f"  {cclass.course.nama}-{cclass.section} di {room.nama} pada {ts}") 
