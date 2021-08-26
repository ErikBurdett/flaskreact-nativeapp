import React, {useState, useEffect} from 'react'
import {StyleSheet, View, Text, Button, FlatList} from 'react-native'
import {Card, FAB} from 'react-native-paper'
//comment for commit
function Home(props) {

    const [data, setData] = useState([])
    const [loading, setIsLoading] = useState(true)

    const loadData = () => {
        fetch('http://192.168.0.4:3000/get', {
            method:'GET'
        })
        .then(resp => resp.json())
        .then(article =>{
            setData(article)
            setIsLoading(false)
        })
        .catch(function(error){
            console.log("error with fetch:" + error.message);
            //throws error
            throw error;
        });

    }

    useEffect(()=>{
        loadData()
    }, [])

    const clickedItem = (data) =>{
        props.navigation.navigate('Details', {data:data})
    }

    const renderData = (item) =>{
        return(
            <Card style={styles.cardStyle}>
                <Text style ={{fontSize:23}} onPress={()=> clickedItem(item)}>{item.title}</Text>
                {/* <Text>{item.body}</Text> */}
            </Card>

        )
    }
    return (
        <View style={{flex:1}}>
            <FlatList
            data = {data}
            renderItem = {({item}) =>{
                return renderData(item)
            }}
            onRefresh = {() => loadData()}
            refreshing = {loading}
            keyExtractor = {item => `${item.id}`}
            />
            <FAB
            style={styles.fab}
            small={false}
            icon="plus"
            theme={{colors:{accent:"green"}}}
            onPress ={()=> props.navigation.navigate('Create')}/>


        </View>
    )
}

export default Home

const styles = StyleSheet.create({
    cardStyle: {
        margin: 10,
        padding: 10,

    },
    fab:{
        position: 'absolute',
        margin: 16,
        right: 0,
        bottom: 0
    }
  });