class Settings():
    def __init__(self):
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 1000
        self.buding_speed_factor = 1
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.fleet_direction = 1
        self.buding_point = 5
        self.yly_point = 10
        self.cat_point = 20
        self.xcw_point = 50
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.buding_speed_factor = 1
        self.fleet_direction = 1
    def increase_speed(self):
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.buding_speed_factor *= self.speedup_scale
        self.xcw_point = int(self.xcw_point*self.score_scale)
        self.buding_point = int(self.buding_point*self.score_scale)