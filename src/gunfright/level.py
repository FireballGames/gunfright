class Bounty:
    dir = [0, 0]
    image = False
    score = 100
    
    def __init__(self, **config):
        if 'image' in config:
            self.image = config['image']
        if 'score' in config:
            self.score = config['score']
        if 'speed' in config:
            import random
            self.dir = [
                random.randrange(*config['speed']['x']), 
                random.randrange(*config['speed']['y'])
            ]


class Level:
    background = False
    
    def __init__(self, **config):
        if 'background' in config:
            self.background = config['background']
    
    def is_finished(self):
        return False
        
    def is_success(self, **args):
        return False


class ShootBounty(Level):
    time = 30000
    score = 1000
    bounties = []
    
    def __init__(self, **config):
        Level.__init__(self, **config)
        if 'time' in config:
            self.time       = config['time']
        if 'score' in config:
            self.score      = config['score']
        if 'bounties' in config:
            self.bounties   = config['bounties']
        if 'player' in config:
            if self.score < config['player'].score:
                self.score += config['player'].score
        
        import pygame
        self.timer = pygame.time.Clock()
            
    def is_finished(self):
        self.time -= self.timer.tick()
        return self.time <= 0
        
    def is_success(self, **args):
        return args['player'].score >= self.score

    def seconds(self):
        return self.time / 1000
                
    def add_bounty(self):
        import random
        p = random.randrange(100)
        for bounty in self.bounties:
            if p < bounty['percent']:
                return Bounty(**bounty)
        return False
