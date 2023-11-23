library(tidyverse)
library(ggplot2)
credit_data <- read.csv("/home/zeddzi/R_credit/Credit-App/credit_card_transaction_flow.csv")
head(credit_data)
summary(credit_data)
str(credit_data)

# Data cleaning
credit_data <- credit_data %>% na.omit()

# Data transformation
credit_data <- credit_data %>% 
  mutate(new_variable = some_transformation(existing_variable))

credit_summary <- credit_data %>% 
  group_by(category_variable) %>% 
  summarise(mean_value = mean(numeric_variable))

# Data visualization
ggplot(credit_data, aes(x = variable1, y = variable2)) +
  geom_point()
