import random
class player:
    def __init__(self,name,position,base_attack,base_defense):
        self.name=name
        self.position=position
        self.base_attack=base_attack
        self.base_defense=base_defense
        self.stamina=100.0
    def deplete_stamina(self,rate=0.5):
            self.stamina-=rate
            if self.stamina<10.0:
                 self.stamina=10.0

    def get_effective_attack(self):
         return float(self.base_attack)*(self.stamina/100.0)


    def get_effective_defense(self):
             return float(self.base_defense)*(self.stamina/100.0)
    

class team:
    def __init__(self,country_name,roster,active_lineup):
            self.country_name=country_name
            if len(roster)!=26:
                  raise ValueError("There must be 26 players in the team")
            self.roster=roster
            if len(active_lineup)!=11:
                raise ValueError("There must be 11 players in the starting  team")
            self.active_lineup=active_lineup
            self.bench = []

            for player in roster:
                if player not in active_lineup:
                     self.bench.append(player)
            self.subs_remaining=5

          
    def get_aggregate_attack(self):
        attack_sum=0
        attack_count=0
        for player in self.active_lineup:
         if player.position=="FORWARD" or player.position=="MIDFIELDER":
             attack_sum+=player.get_effective_attack()
             attack_count+=1
        self.final=attack_sum/attack_count
        return self.final     
    def get_aggregate_defense(self):
        defense_sum=0
        defense_count=0
        for player in self.active_lineup:
              if player.position=="DEFENDER" or player.position=="GOALKEEPER":
                   defense_sum+=player.get_effective_defense()
                   defense_count+=1

        return defense_sum/defense_count  
    def execute_substitution(self,player_out,player_in):
        if self.subs_remaining>0 and player_out in self.active_lineup and player_in in self.bench :
              self.active_lineup.remove(player_out)
              self.bench.append(player_out)
              self.active_lineup.append(player_in) 
              self.bench.remove(player_in)
              self.subs_remaining-=1
        else:
             raise ValueError("check that substitution conditions are true")


class MatchEvent:
    def __init__(self, event_id, event_type, minute, team, player, outcome_text):
        self.event_id = event_id
        self.event_type = event_type
        self.minute = minute
        self.team = team
        self.player = player
        self.outcome_text = outcome_text
          
    def to_string(self):
         if self.event_type=="GOAL":
            return f"At minute {self.minute} {self.team.country_name} scored By {self.player.name}"
         elif self.event_type == "SUBSTITUTION":
            return f"At minute {self.minute}, {self.team.country_name} made a substitution."
         elif self.event_type == "HALF_TIME":
            return f"Half Time - {self.minute}"
         elif self.event_type == "FULL_TIME":
            return f"Full Time - {self.minute}"
         
class match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
        self.current_minute = 0
        self.phase = "REGULATION"
        self.timeline = []  

    def run_minute_tick(self):
     if self.phase == "FINISHED":
        raise ValueError("match is already finished")
     if self.current_minute<=89:   
         self.current_minute+=1
     else:
         raise ValueError("minutes out of range")     
     
     for player in self.home_team.active_lineup:
               player.deplete_stamina() 

     for player in self.away_team.active_lineup:
                player.deplete_stamina()

     self.process_goal_attempt(self.home_team, self.away_team)
     self.process_goal_attempt(self.away_team, self.home_team)

     if self.current_minute == 90:
        self.phase = "FINISHED"
        if self.home_score > self.away_score:
            self.result = f"{self.home_team.country_name} wins"
        elif self.away_score > self.home_score:
            self.result = f"{self.away_team.country_name} wins"
        else:
            self.result = "DRAW"

    def process_goal_attempt(self, attacking_team, defending_team):
  
     if random.random() < 0.10:
        aggregate_attack = attacking_team.get_aggregate_attack()
        aggregate_defense = defending_team.get_aggregate_defense()

        attack_roll = aggregate_attack * random.uniform(0.75, 1.25)
        defense_roll = aggregate_defense * 1.3 * random.uniform(0.80, 1.20) # ai helped me with this function because i really couldnt know how too deal with random

        if attack_roll > defense_roll:
            if attacking_team == self.home_team:
                self.home_score += 1
            else:
                self.away_score += 1

            scorer = attacking_team.active_lineup[0]
            outcome_text = f"{scorer.name} scores for {attacking_team.country_name}!"
            event_id=1
            goal_event = MatchEvent(
                event_id, "GOAL", self.current_minute,attacking_team, scorer, outcome_text
            )
            self.timeline.append(goal_event)   
    
messi = player("Messi","FORWARD",95,30)
alvarez = player("Alvarez","FORWARD",85,35)
enzo = player("Enzo","MIDFIELDER",80,60)
romero = player("Romero","DEFENDER",30,90)
otamendi = player("Otamendi","DEFENDER",25,88)
tagliafico = player("Tagliafico","DEFENDER",20,82)
molina = player("Molina","DEFENDER",30,80)
martinez = player("Martinez","GOALKEEPER",10,95)
p1 = player("P1","MIDFIELDER",75,55)
p2 = player("P2","MIDFIELDER",70,60)
p3 = player("P3","MIDFIELDER",72,58)

lineup = [
messi,alvarez,enzo,p1,p2,p3,
romero,otamendi,tagliafico,molina,martinez
]
dybala = player("Dybala","FORWARD",90,35)
lautaro = player("Lautaro","FORWARD",91,38)
garnacho = player("Garnacho","FORWARD",87,30)

palacios = player("Palacios","MIDFIELDER",78,76)
lo_celso = player("Lo Celso","MIDFIELDER",80,72)
mac_allister = player("Mac Allister","MIDFIELDER",84,78)
paredes = player("Paredes","MIDFIELDER",75,82)

pezzella = player("Pezzella","DEFENDER",30,86)
foyth = player("Foyth","DEFENDER",32,84)
senesi = player("Senesi","DEFENDER",29,87)
lisandro = player("Lisandro","DEFENDER",34,91)
montiel = player("Montiel","DEFENDER",31,83)

rulli = player("Rulli","GOALKEEPER",10,90)
musso = player("Musso","GOALKEEPER",10,89)

correa = player("Correa","FORWARD",84,36)
argentina_roster = lineup + [
    dybala,
    lautaro,
    garnacho,
    palacios,
    lo_celso,
    mac_allister,
    paredes,
    pezzella,
    foyth,
    senesi,
    lisandro,
    montiel,
    rulli,
    musso,
    correa
]

argentina = team("Argentina", argentina_roster, lineup)

mbappe = player("Mbappe","FORWARD",100,35)
dembele = player("Dembele","FORWARD",100,40)
griezmann = player("Griezmann","MIDFIELDER",100,65)
camavinga = player("Camavinga","MIDFIELDER",100,80)
tchouameni = player("Tchouameni","MIDFIELDER",78,84)
rabiot = player("Rabiot","MIDFIELDER",75,82)

hernandez = player("Hernandez","DEFENDER",35,91)
upamecano = player("Upamecano","DEFENDER",32,89)
konate = player("Konate","DEFENDER",30,88)
kounde = player("Kounde","DEFENDER",38,86)

maignan = player("Maignan","GOALKEEPER",10,96)
france_lineup = [
    mbappe,
    dembele,
    griezmann,
    camavinga,
    tchouameni,
    rabiot,
    hernandez,
    upamecano,
    konate,
    kounde,
    maignan
]
bench = [
    player("Coman","FORWARD",87,40),
    player("Thuram","FORWARD",86,42),
    player("Muani","FORWARD",84,38),
    player("Olise","MIDFIELDER",83,60),
    player("Fofana","MIDFIELDER",79,78),
    player("Zaire-Emery","MIDFIELDER",80,76),
    player("Saliba","DEFENDER",35,94),
    player("Pavard","DEFENDER",34,89),
    player("Disasi","DEFENDER",30,85),
    player("Clauss","DEFENDER",32,84),
    player("Lucas","DEFENDER",28,87),
    player("Samba","GOALKEEPER",10,90),
    player("Areola","GOALKEEPER",10,88),
    player("Nkunku","FORWARD",89,45),
    player("Barcola","FORWARD",85,39)
]
france_roster = france_lineup + bench

france = team("France", france_roster, france_lineup)

match1=match(france,argentina)
for i in range(90):
    match1.run_minute_tick()
print(match1.current_minute)
print(match1.home_score,end=' ')
print(match1.away_score)
print(match1.phase)
for i in match1.timeline:
    print(i.to_string()) 
