# py---2---web-20-00--mini-social

> relations

        * direct / indirect --> when we can call the object directly without some additional code
        * forward / backward --> direction starts always from the most important entity -- in that case is user, without user can't exist anything
        * many / one  --> user-post is a one-many relations,  post-user is a many-one relation


+-------------------DOMAIN-----------------------------------------------------------+       
|                                                                                    |           
|   +----------------------------------------------------+                           |           
|   |  +--------------------------------+                |                           |           
|   |  |                                |                |                           | 
|   |  |                                |                v                           | 
|   |  |                                v --------------....----------+              | 
|   |  |     User  <-----------+       Post            Comment        |              |          
|   |  |        * id           |         * id            * id         |              |               
|   |  |        * username     |         * title         * body       |              |                        
|   |  |        * email        |         * body                       |              |                      
|   |  |        * password     +-------------------->    * user       |              |                   
|   |  |                       +-------> *user           * post ------+              |                                              
|   |  +------  * posts[]                                                            |              
|   +---------  * comments[]                                                         |             
|                                                   All realtions are direct!!!      |+------------------------------------------------------------------------------------+ 







> behavior

+-------------------DOMAIN-----------------------------------------------------------+       
|                                                                                    |           
|                                                                                    |                           
|                                                                                    |                                       
|    user<User>.addPost(self, postId, postTitle, postBody)                           |                                   
|     |                   ^|                                                         |                       
|     |                   |+--------------------------------------V                  |                               
|     +-------------------+   Post(postId, postTitle, postBody, self)                |                               
|                                                v                                   |                                           
|                                                post<Post>                          |                                                               
|                                                                                    |                               
|                                                                                    |                   
|    user<User>.addComment(self, commId, commBody, commPost)                         |                                                   
|     |                   ^|                                                         |                                       
|     |                   |+--------------------------------------V                  |                                   
|     +-------------------+   Comment(commId, commBody, self, commPost)              |                                               
|                                                v                                   |                                   
|                                          comment<Comment>                          |
|                                                                                    |
+------------------------------------------------------------------------------------+                                          