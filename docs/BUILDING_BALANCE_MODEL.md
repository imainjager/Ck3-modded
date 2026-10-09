# Building balance model (derived from vanilla) and Irish targets
Proposed for UPDATE 4. Every Irish building is built from a vanilla analogue: same cost curve, headline numbers about **+30%** (the user's rough suggestion, not a fixed rule), plus one Irish flavor effect. Integer stats (fort level, knight limit) stay the same and gain a second effect instead.

## Scaling rules read from vanilla
* **Cost curve (gold):** economy, military, temple and administrative chains cost 150 / 250 / 340 / 500 / 750 / 1110 / 1600 / 2240 for levels I-VIII. Fortification chains cost 100 / 150 / 195 / 275 / 400 / 580 / 825 / 1145. Tribal chains cost 75 / 100 / 125 / 150 gold **plus 200 / 350 prestige** at levels I and II. Duchy-capital chains cost 485 / 725 / 1100 (three levels). Specials cost 1000 (most), 300-800 (small ones), 2000-3000 (wonders).
* **Level step:** income grows by about +0.2/month per level (0.35 at I, 0.55 at II ... 1.75 at VIII). Defender advantage +2 per level, fort level +1 per level, travel danger -1 per level, piety +0.1 per level, county control growth +0.1 per level for the first four levels, knight effectiveness +2% per level, levies 100 / 175 / 175 / 225 ... 425, garrison 150 / 300 / 450 / 800 ...
* **Effects per building:** a regular building has 4-5 distinct effects (median); duchy buildings 3-8; special buildings 8 or more in 41% of cases. So 'a building does one thing' is never right: the headline effect plus 3-4 side effects is the norm.
* **Duchy chains:** three levels, +10/20/30% development growth across the duchy or +15/20/30% tax, +5/10/15 county opinion, +4/8/12 court grandeur. **Specials:** county development growth +10% to +30% (median 20%), monthly income +2 (median), county tax +15% to +20%, character piety +0.25 to +1.
* **The Irish rule:** headline numbers x1.3 of the analogue at the same level, same gold cost curve, prestige added only where the building is tribal (vanilla's own tribal pattern), and exactly one Irish effect (legend spread, fosterage opinion, bardic prestige, cattle levy, poet opinion, hospitality) that has no vanilla analogue.

## Vanilla analogues and the Irish targets (x1.3)

### Dún (hill-fort) (analogue: `palisades`, tribal fort)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 75g+200p | defender_holding_advantage 2, fort_level 1, levy 100, max_garrison 150 | defender_holding_advantage 2.6, fort_level 1, levy 130, max_garrison 195 |
| 2 | 100g+350p | defender_holding_advantage 4, fort_level 2, levy 175, max_garrison 300 | defender_holding_advantage 5.2, fort_level 2, levy 228, max_garrison 390 |

### Ringfort (analogue: `hill_forts`, all holdings)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 100g | defender_holding_advantage 2, fort_level 2, travel_danger -1, max_garrison 250 | defender_holding_advantage 2.6, fort_level 2, travel_danger -1.3, max_garrison 325 |
| 2 | 150g | defender_holding_advantage 4, fort_level 4, travel_danger -2, monthly_county_control_growth_factor 0.1, monthly_county_control_decline_factor -0.1, max_garrison 500 | defender_holding_advantage 5.2, fort_level 4, travel_danger -2.6, monthly_county_control_growth_factor 0.13, monthly_county_control_decline_factor -0.13, max_garrison 650 |
| 3 | 195g | defender_holding_advantage 6, fort_level 6, travel_danger -3, monthly_county_control_growth_factor 0.1, monthly_county_control_decline_factor -0.1, max_garrison 750 | defender_holding_advantage 7.8, fort_level 6, travel_danger -3.9, monthly_county_control_growth_factor 0.13, monthly_county_control_decline_factor -0.13, max_garrison 975 |

### Crannóg stronghold (analogue: `ramparts`, all holdings)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 100g | fort_level 1, travel_danger -1, levy 100, max_garrison 150 | fort_level 1, travel_danger -1.3, levy 130, max_garrison 195 |
| 2 | 150g | fort_level 2, tax_mult 0.02, travel_danger -2, levy 175, max_garrison 300 | fort_level 2, tax_mult 0.026, travel_danger -2.6, levy 228, max_garrison 390 |
| 3 | 195g | fort_level 3, defender_holding_advantage 2, tax_mult 0.02, travel_danger -3, levy 250, max_garrison 450 | fort_level 3, defender_holding_advantage 2.6, tax_mult 0.026, travel_danger -3.9, levy 325, max_garrison 585 |

### Round Tower (analogue: `watchtowers`, all holdings)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 100g | defender_holding_advantage 2, fort_level 1, travel_danger -1, max_garrison 150 | defender_holding_advantage 2.6, fort_level 1, travel_danger -1.3, max_garrison 195 |
| 2 | 150g | defender_holding_advantage 4, fort_level 2, travel_danger -2, hostile_raid_time 0.1, max_garrison 300 | defender_holding_advantage 5.2, fort_level 2, travel_danger -2.6, hostile_raid_time 0.13, max_garrison 390 |
| 3 | 195g | defender_holding_advantage 6, fort_level 3, travel_danger -3, hostile_raid_time 0.1, max_garrison 450 | defender_holding_advantage 7.8, fort_level 3, travel_danger -3.9, hostile_raid_time 0.13, max_garrison 585 |

### Aonach fair ground (analogue: `market_villages`, tribal market)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 75g+200p | monthly_income 0.4, supply_limit 500 | monthly_income 0.52, supply_limit 650 |
| 2 | 100g+350p | monthly_income 0.7, supply_limit 1000 | monthly_income 0.91, supply_limit 1300 |

### Booley pastures (analogue: `pastures`, economy)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | monthly_income 0.35, supply_limit 200, levy 75 | monthly_income 0.455, supply_limit 260, levy 97.5 |
| 2 | 250g | monthly_income 0.55, supply_limit 400, levy 125 | monthly_income 0.715, supply_limit 520, levy 162 |
| 3 | 340g | monthly_income 0.75, supply_limit 600, levy_reinforcement_rate 0.1, levy 175 | monthly_income 0.975, supply_limit 780, levy_reinforcement_rate 0.13, levy 228 |

### Fosterage Hall (analogue: `longhouses`, tribal)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 75g+200p | monthly_county_control_growth_add 0.2, monthly_prestige 0.25, levy 100 | monthly_county_control_growth_add 0.26, monthly_prestige 0.325, levy 130 |
| 2 | 100g+350p | monthly_county_control_growth_add 0.4, monthly_prestige 0.5, levy 175 | monthly_county_control_growth_add 0.52, monthly_prestige 0.65, levy 228 |

### Smithy of Goibniu (analogue: `smiths`, military economy)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | tax_mult 0.04, levy_reinforcement_rate 0.1, knight_effectiveness_mult 0.01 | tax_mult 0.052, levy_reinforcement_rate 0.13, knight_effectiveness_mult 0.013 |
| 2 | 250g | tax_mult 0.08, levy_reinforcement_rate 0.15, knight_effectiveness_mult 0.02 | tax_mult 0.104, levy_reinforcement_rate 0.195, knight_effectiveness_mult 0.026 |
| 3 | 340g | tax_mult 0.12, levy_reinforcement_rate 0.2, knight_effectiveness_mult 0.03 | tax_mult 0.156, levy_reinforcement_rate 0.26, knight_effectiveness_mult 0.039 |

### Hobby stables (analogue: `stables`, military)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | movement_speed 0.01, character_travel_speed_mult 0.01, levy 100 | movement_speed 0.013, character_travel_speed_mult 0.013, levy 130 |
| 2 | 250g | movement_speed 0.02, character_travel_speed_mult 0.02, levy 175 | movement_speed 0.026, character_travel_speed_mult 0.026, levy 228 |
| 3 | 340g | movement_speed 0.03, character_travel_speed_mult 0.03, levy 250 | movement_speed 0.039, character_travel_speed_mult 0.039, levy 325 |

### Monastic school (analogue: `monastic_schools`, temple)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | monthly_income 0.25, epidemic_resistance 4, monthly_county_control_growth_add 0.1, monthly_piety 0.1 | monthly_income 0.325, epidemic_resistance 5.2, monthly_county_control_growth_add 0.13, monthly_piety 0.13 |
| 2 | 250g | monthly_income 0.4, epidemic_resistance 6, monthly_county_control_growth_add 0.2, monthly_piety 0.2 | monthly_income 0.52, epidemic_resistance 7.8, monthly_county_control_growth_add 0.26, monthly_piety 0.26 |
| 3 | 340g | monthly_income 0.55, epidemic_resistance 8, monthly_county_control_growth_add 0.3, monthly_piety 0.3 | monthly_income 0.715, epidemic_resistance 10.4, monthly_county_control_growth_add 0.39, monthly_piety 0.39 |

### Hermitage / Scriptorium (analogue: `scriptorium`, temple)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | monthly_county_control_growth_add 0.1, monthly_piety 0.1 | monthly_county_control_growth_add 0.13, monthly_piety 0.13 |
| 2 | 250g | monthly_county_control_growth_add 0.2, monthly_piety 0.2 | monthly_county_control_growth_add 0.26, monthly_piety 0.26 |
| 3 | 340g | monthly_county_control_growth_add 0.3, monthly_piety 0.3 | monthly_county_control_growth_add 0.39, monthly_piety 0.39 |

### Pilgrim hospice (analogue: `hospices`, common)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | monthly_income 0.25, epidemic_resistance 5, monthly_piety 0.1 | monthly_income 0.325, epidemic_resistance 6.5, monthly_piety 0.13 |
| 2 | 250g | monthly_income 0.4, epidemic_resistance 7, monthly_piety 0.2 | monthly_income 0.52, epidemic_resistance 9.1, monthly_piety 0.26 |
| 3 | 340g | monthly_income 0.55, epidemic_resistance 10, monthly_piety 0.3 | monthly_income 0.715, epidemic_resistance 13, monthly_piety 0.39 |

### Ogham pillar field (analogue: `megalith`, temple)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | development_growth_factor 0.02, county_opinion_add 2, monthly_piety 0.25 | development_growth_factor 0.026, county_opinion_add 2.6, monthly_piety 0.325 |
| 2 | 250g | development_growth_factor 0.05, county_opinion_add 2, monthly_piety 0.4 | development_growth_factor 0.065, county_opinion_add 2.6, monthly_piety 0.52 |
| 3 | 340g | development_growth_factor 0.1, county_opinion_add 4, monthly_piety 0.55 | development_growth_factor 0.13, county_opinion_add 5.2, monthly_piety 0.715 |

### Irish Sea quay (analogue: `common_tradeport`, economy)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | monthly_income 0.35, development_growth_factor 0.05 | monthly_income 0.455, development_growth_factor 0.065 |
| 2 | 250g | monthly_income 0.55, development_growth_factor 0.1 | monthly_income 0.715, development_growth_factor 0.13 |
| 3 | 340g | monthly_income 0.75, development_growth_factor 0.15 | monthly_income 0.975, development_growth_factor 0.195 |

### Longship yard (analogue: `kora_kora_yards`, tribal)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 75g | monthly_barter_goods 0.25, defender_holding_advantage 1, naval_movement_speed_mult 0.1, monthly_barter_goods_mult 0.01, raid_speed 0.1, levy 125 | monthly_barter_goods 0.325, defender_holding_advantage 1.3, naval_movement_speed_mult 0.13, monthly_barter_goods_mult 0.013, raid_speed 0.13, levy 162 |
| 2 | 100g | monthly_barter_goods 0.5, defender_holding_advantage 2, naval_movement_speed_mult 0.2, monthly_barter_goods_mult 0.02, raid_speed 0.2, levy 225 | monthly_barter_goods 0.65, defender_holding_advantage 2.6, naval_movement_speed_mult 0.26, monthly_barter_goods_mult 0.026, raid_speed 0.26, levy 292 |
| 3 | 125g | monthly_barter_goods 0.7, defender_holding_advantage 3, naval_movement_speed_mult 0.3, monthly_barter_goods_mult 0.03, raid_speed 0.3, levy 325 | monthly_barter_goods 0.91, defender_holding_advantage 3.9, naval_movement_speed_mult 0.39, monthly_barter_goods_mult 0.039, raid_speed 0.39, levy 422 |

### Bruidhean hostel (analogue: `caravanserai`, economy)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 200g | monthly_income 0.7, defender_holding_advantage 2, development_growth_factor 0.04, development_growth 0.02, travel_danger -1, men_at_arms_maintenance -0.008 | monthly_income 0.91, defender_holding_advantage 2.6, development_growth_factor 0.052, development_growth 0.026, travel_danger -1.3, men_at_arms_maintenance -0.01 |
| 2 | 350g | monthly_income 1.15, defender_holding_advantage 4, development_growth_factor 0.08, development_growth 0.04, travel_danger -2, men_at_arms_maintenance -0.016 | monthly_income 1.49, defender_holding_advantage 5.2, development_growth_factor 0.104, development_growth 0.052, travel_danger -2.6, men_at_arms_maintenance -0.021 |
| 3 | 485g | monthly_income 1.6, defender_holding_advantage 6, hostile_raid_time 0.2, development_growth_factor 0.12, development_growth 0.06, travel_danger -3 | monthly_income 2.08, defender_holding_advantage 7.8, hostile_raid_time 0.26, development_growth_factor 0.156, development_growth 0.078, travel_danger -3.9 |

### Cattle enclosure (analogue: `hill_farms`, economy)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 100g | monthly_income 0.35 | monthly_income 0.455 |
| 2 | 150g | monthly_income 0.55, defender_holding_advantage 1 | monthly_income 0.715, defender_holding_advantage 1.3 |
| 3 | 195g | monthly_income 0.75, defender_holding_advantage 1, supply_limit 300 | monthly_income 0.975, defender_holding_advantage 1.3, supply_limit 390 |

### Holy well (analogue: `temple`, temple)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 400g | monthly_income 0.75, travel_danger -10, levy 50, max_garrison 150 | monthly_income 0.975, travel_danger -13, levy 65, max_garrison 195 |
| 2 | 550g | monthly_income 1.15, travel_danger -12, levy 100, max_garrison 450 | monthly_income 1.49, travel_danger -15.6, levy 130, max_garrison 585 |
| 3 | 700g | monthly_income 1.55, travel_danger -14, levy 150, max_garrison 750 | monthly_income 2.01, travel_danger -18.2, levy 195, max_garrison 975 |

### War-band hall (Fianna lodge) (analogue: `warrior_lodges`, military)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 100g | travel_danger -1, levy 100 | travel_danger -1.3, levy 130 |
| 2 | 150g | travel_danger -2, levy 175 | travel_danger -2.6, levy 228 |
| 3 | 195g | travel_danger -3, levy 250 | travel_danger -3.9, levy 325 |

### Brehon court (analogue: `guild_halls`, city)
| Level | Vanilla cost | Vanilla effects | Irish target effects (x1.3) |
|---|---|---|---|
| 1 | 150g | monthly_income 0.35, development_growth_factor 0.05 | monthly_income 0.455, development_growth_factor 0.065 |
| 2 | 250g | monthly_income 0.55, development_growth_factor 0.1 | monthly_income 0.715, development_growth_factor 0.13 |
| 3 | 340g | monthly_income 0.75, development_growth_factor 0.15 | monthly_income 0.975, development_growth_factor 0.195 |

## Duchy-capital targets
| Level | Vanilla gold | Vanilla (development growth / opinion / grandeur) | Irish target |
|---|---|---|---|
| 1 | 485 | +10% development growth, +5 county opinion, +4 grandeur | +13% development growth, +6 county opinion, +5 grandeur, plus one Irish effect |
| 2 | 725 | +20% development growth, +10 county opinion, +8 grandeur | +26% development growth, +13 county opinion, +10 grandeur, plus one Irish effect |
| 3 | 1100 | +30% development growth, +15 county opinion, +12 grandeur | +39% development growth, +20 county opinion, +16 grandeur, plus one Irish effect |

## Special-building targets
Vanilla median: 1000 gold, county development growth +20%, income +2/month, county tax +20%, piety +0.25 to +1, 8 effects. Irish target: 1000 gold, county development growth +26%, income +2.6/month, county tax +26%, piety +0.33 to +1.3, 8 effects including one Irish effect (legend spread, dynasty prestige, bardic prestige or clergy opinion).
