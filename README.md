# pushdown-automata

```
\documentclass[12pt]{article}
\usepackage{tikz}

\begin{document}

\begin{center}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (9.8,-12.6) circle (3);
\draw (9.8,-12.6) node {$q_0$};
\draw [black] (31.1,-12.6) circle (3);
\draw (31.1,-12.6) node {$q_1$};
\draw [black] (48,-12.6) circle (3);
\draw (48,-12.6) node {$q2$};
\draw [black] (66.7,-12.6) circle (3);
\draw (66.7,-12.6) node {$q3$};
\draw [black] (66.7,-28.1) circle (3);
\draw (66.7,-28.1) node {$q4$};
\draw [black] (53.5,-33.2) circle (3);
\draw (53.5,-33.2) node {$q_5$};
\draw [black] (42.3,-33.2) circle (3);
\draw (42.3,-33.2) node {$q_6$};
\draw [black] (26.5,-33.2) circle (3);
\draw (26.5,-33.2) node {$q_7$};
\draw [black] (11.3,-46.7) circle (3);
\draw (11.3,-46.7) node {$q_8$};
\draw [black] (36.7,-46.7) circle (3);
\draw (36.7,-46.7) node {$F$};
\draw [black] (36.7,-46.7) circle (2.4);
\draw [black] (51,-12.6) -- (63.7,-12.6);
\fill [black] (63.7,-12.6) -- (62.9,-12.1) -- (62.9,-13.1);
\draw (57.35,-12.1) node [above] {$(\w|\d)$};
\draw [black] (66.7,-15.6) -- (66.7,-25.1);
\fill [black] (66.7,-25.1) -- (67.2,-24.3) -- (66.2,-24.3);
\draw (67.2,-20.35) node [right] {$(<|>|==)$};
\draw [black] (12.8,-12.6) -- (28.1,-12.6);
\fill [black] (28.1,-12.6) -- (27.3,-12.1) -- (27.3,-13.1);
\draw (20.45,-13.1) node [below] {$while,\mbox{ }\epsilon\mbox{ }->$$};
\draw [black] (34.1,-12.6) -- (45,-12.6);
\fill [black] (45,-12.6) -- (44.2,-12.1) -- (44.2,-13.1);
\draw (39.55,-13.1) node [below] {$($};
\draw [black] (63.9,-29.18) -- (56.3,-32.12);
\fill [black] (56.3,-32.12) -- (57.22,-32.3) -- (56.86,-31.36);
\draw (57.13,-30.08) node [above] {$(\w|\d)$};
\draw [black] (50.5,-33.2) -- (45.3,-33.2);
\fill [black] (45.3,-33.2) -- (46.1,-33.7) -- (46.1,-32.7);
\draw (47.9,-32.7) node [above] {$)$};
\draw [black] (39.3,-33.2) -- (29.5,-33.2);
\fill [black] (29.5,-33.2) -- (30.3,-33.7) -- (30.3,-32.7);
\draw (34.4,-32.7) node [above] {${,\epsilon->{$};
\draw [black] (27.15,-30.27) -- (30.45,-15.53);
\fill [black] (30.45,-15.53) -- (29.78,-16.2) -- (30.76,-16.42);
\draw (29.55,-23.28) node [right] {$while$};
\draw [black] (24.26,-35.19) -- (13.54,-44.71);
\fill [black] (13.54,-44.71) -- (14.47,-44.55) -- (13.81,-43.8);
\draw (15.86,-39.46) node [above] {$},{->\epsilon$};
\draw [black] (11.17,-43.7) -- (9.93,-15.6);
\fill [black] (9.93,-15.6) -- (9.47,-16.42) -- (10.47,-16.37);
\draw (11.12,-29.63) node [right] {$while$};
\draw [black] (14.3,-46.7) -- (33.7,-46.7);
\fill [black] (33.7,-46.7) -- (32.9,-46.2) -- (32.9,-47.2);
\draw (24,-47.2) node [below] {$\epsilon,$->\epsilon$};
\end{tikzpicture}
\end{center}

\end{document}

```
