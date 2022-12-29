class Grid:
    def __init__(self, filename):
        self.read(filename)
        #self.check_grid_test2()

    def get_score(self):
        score = 0

        score += 2* self.rows + 2 * self.cols - 4
        for r in range(1, self.rows-1):
            for c in range(1, self.cols-1):
                if self.check_grid_val(r, c):
                    score += 1

        return score

    def read(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f.readlines()]

        self.rows = len(lines)
        self.cols = len(lines[0])

        self.grid = []

        for line in lines:
            row = [int(c) for c in line]
            self.grid.append(row)

    def check_grid_test(self):
        for (r, c) in \
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 2),
            ]:
            print(self.check_grid_val(r, c))

    def check_grid_test2(self):
        for (r, c) in \
                [
                    (1, 2),
                    (3, 2),
                ]:
            print('viewing dist of ', (r,c), self.check_grid_val_viewing_dist(r, c))

    def check_vals(self, target, val_list):
        for (r, c) in val_list:
            if self.grid[r][c] >= target: # not visible
                return False
        return True

    def check_grid_val(self, row, col):
        val = self.grid[row][col]

        visible = False

        # up
        if row > 0 and self.check_vals(val, [(r, col) for r in range(0, row)]):
            visible = True
        # down
        if row < self.rows - 1 and self.check_vals(val, [(r, col) for r in range(row+1, self.rows)]):
            visible = True

        # left
        if col > 0 and self.check_vals(val, [(row, c) for c in range(0, col)]):
            visible = True
        # right
        if col < self.cols - 1 and self.check_vals(val, [(row, c) for c in range(col+1, self.cols)]):
            visible = True
        return visible

    def get_score2(self):
        max_score = -1
        for r in range(1, self.rows-1):
            for c in range(1, self.cols-1):
                score = self.check_grid_val_viewing_dist(r, c)
                if score > max_score:
                    max_score = score
        return max_score


    def check_grid_val_viewing_dist(self, row, col):

        def check_vals(target, val_list):
            view = 0
            for (r, c) in val_list:
                view += 1
                if self.grid[r][c] >= target:  # not visible
                    break
            return view

        val = self.grid[row][col]

        visible = False

        view_dist_score = 1

        # up
        if row > 0:
            view_dist_score *= check_vals(val, [(r, col) for r in range(row-1, -1, -1)])

        # down
        if row < self.rows - 1:
            view_dist_score *= check_vals(val, [(r, col) for r in range(row+1, self.rows)])

        # left
        if col > 0:
            view_dist_score *= check_vals(val, [(row, c) for c in range(col-1, -1, -1)])

        # right
        if col < self.cols - 1:
            view_dist_score *= check_vals(val, [(row, c) for c in range(col+1, self.cols)])

        return view_dist_score

def score(filename):
    grid = Grid(filename)
    print(grid.get_score())
    print(grid.get_score2())

score('sample.txt')
score('input.txt')
