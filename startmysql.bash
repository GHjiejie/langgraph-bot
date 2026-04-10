docker run -d \
  --name langgraph-mysql \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -e MYSQL_DATABASE=langgraph_bot \
  mysql:9.6.0  \
  --character-set-server=utf8mb4 \
  