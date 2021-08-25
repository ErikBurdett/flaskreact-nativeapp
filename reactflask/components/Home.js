import React, {useState} from 'react'
import {StyleSheet, View, Text, Button, FlatList} from 'react-native'
import {Card, FAB} from 'react-native-paper'

function Home(props) {
    const data = [
        {id: 1,title: '1 Title', body: 'First Body'},
        {id: 2,title: '2 Title', body: 'Second Body'},
        {id: 3,title: '3 Title', body: 'Third Body'}
    ]

    const renderData = (item) =>{
        return(
            <Card style={styles.cardStyle}>
                <Text style ={{fontSize:20}}>{item.title}</Text>
                <Text>{item.body}</Text>
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
            keyExtractor = {item => `${item.id}`}
            />
            <FAB
            style={styles.fab}
            small={false}
            icon="plus"
            theme={{colors:{accent:"green"}}}
            onPress ={()=> console.log('pressed')}/>


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