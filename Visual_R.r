library(ggplot2)

df <- read.csv('Netflix_shows_movies_clean.csv')
ggplot(df, aes(x = rating)) +
  geom_bar(fill = 'blue', color = 'black') +
  ggtitle('Ratings Distribution') +
  xlab('Rating') +
  ylab('Frequency') +
  theme_minimal(base_size = 15) +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())



