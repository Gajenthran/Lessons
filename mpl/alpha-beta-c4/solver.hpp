#ifndef SOLVER_H_
#define SOLVER_H_

#include "grid.hpp"

class Solver {
public:
  Solver();

  int evaluate(Grid &g);
  int maxChild(Grid &g, int col, int alpha, int beta);
  int maxFirst(Grid &g, int alpha, int beta);
  int minFirst(Grid &g, int alpha, int beta);
  int max(Grid &g, int alpha, int beta);
  int min(Grid &g, int alpha, int beta);
  int maxNodes(Grid &g, int alpha, int beta);
  int getBestChild(std::vector<int>& v);
  int computerMove(Grid &g, int thread);

  class GameTree {
  public:
    int nbNodes_;
    int alpha_;
    int beta_;
    int bestMove_;
  };

  auto gameTree(int nbNodes, int alpha, int beta, int bestMove) {
    return GameTree { nbNodes, alpha, beta, bestMove, *this };
  }
private:
	int colOder_[W];
};

#endif