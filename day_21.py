def total_steps(garden, steps):
    garden.insert(0, list("#" * len(garden[0])))
    garden.append(list("#" * len(garden[0])))
    garden = [["#", *r, "#"] for r in garden]
    
    y = [i for i, r in enumerate(garden) if "S" in r][0]
    x = [i for i, c in enumerate(garden[y]) if "S" == c][0]

    def flood_fill(x, y, current_steps):
        if garden[y][x] == "#":
            return
        if current_steps == steps:
            garden[y][x] = "O"
            return
        flood_fill(x + 1, y, current_steps + 1)
        flood_fill(x - 1, y, current_steps + 1)
        flood_fill(x, y + 1, current_steps + 1)
        flood_fill(x, y - 1, current_steps + 1)
        
    flood_fill(x, y, 0)

    return sum(r.count("O") for r in garden)
    
