from neo4j import GraphDatabase


def main(params):

     neo4j_uri = 'neo4j+s://a2903c3d.databases.neo4j.io'
     neo4j_user = 'neo4j'
     neo4j_password = 'x7lO8GKrglcmm4MYuHcBp_PJx23STanbAUKfnuj_FIg'
     driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
     details = []
     agency = "X"
     title = "Please select "
   #  with driver.session() as session:
    #      if agency:
            #   details = get_versions(session, agency)
               #title += "a version"
               
     return {
          # specify headers for the HTTP response
          # we only set the Content-Type in this case, to 
          # ensure the text is properly displayed in the browser
          "headers": {
              "Content-Type": "text/plain;charset=utf-8",
          },
          
          ## use the text generator to create a response sentence
          #  with 10 words
          "body": "details"
      }
