# Skip This if using the current folder
mvn archetype:generate \
-DgroupId=com.example \
-DartifactId=myapp \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false

# Run from here

mvn compile
mvn test
mvn package
mvn exec:java -Dexec.mainClass="com.example.App"
