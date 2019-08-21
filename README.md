# Empire Cinemas 'Now Showing' Webpage Scraper
A Python webpage scraper utilising Beautiful Soup.

Prints a formatted list (titles and descriptions) of all the films in the 'Now Showing' section of a cinema locations webpage.

## Usage
1. Navigate to the [Empire Cinemas](https://www.empirecinemas.co.uk/) website and choose a cinema location.
2. Navigate to the 'Now Showing' page for the given location.
3. Copy the URL into the `url` variable at the top of the script
4. Run the script

## Example Output
What follows is an example output of the script for the High Wycombe location (url: https://www.empirecinemas.co.uk/nowshowing/t2).

>1) Fast & Furious: Hobbs & Shaw                                                                                              
>                                                                                                                             
>Lawman Luke Hobbs and outcast Deckard Shaw form an unlikely alliance when a cyber-genetically enhanced villain threatens the 
>future of humanity.                                                                                                          
>                                                                                                                             
>2) The Lion King                                                                                                             
>                                                                                                                             
>Disney invites you to experience an all-new live action version of the global phenomenon.  Prepare to journey to the African 
>savannah where a future king is born.                                                                                        
>                                                                                                                             
>3) Toy Story 4                                                                                                               
>                                                                                                                             
>When a new toy called qForkyq joins Woody and the gang, a road trip alongside old and new friends reveals how big the world c
>an be for a toy.                                                                                                             
>                                                                                                                             
>4) Blinded By The Light                                                                                                      
>                                                                                                                             
>In 1987 during the austere days of Thatcher's Britain, a teenager learns to live life, understand his family and find his own
> voice through the music of Bruce Springsteen.                                                                               
>                                                                                                                             
>5) Angry Birds 2                                                                                                             
>                                                                                                                             
>The flightless birds and scheming green pigs take their beef to the next level.
