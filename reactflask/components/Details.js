import React from 'react'
import {View, ScrollView, Text, StyleSheet} from 'react-native'
import {TextInput, Button} from 'react-native-paper'
function Details(props) {
    const data = props.route.params.data;
    return (
        <ScrollView>
            <View style={styles.viewStyle}>
                <Text style={{fontSize:25}}>
                    {data.title}
                </Text>
                <Text style={{fontSize:20, marginTop:10}}>
                    {data.body}
                </Text>
                <Text style={{fontSize:15, marginTop:10}}>
                    {data.date}
                </Text>
                <View style={styles.btnStyle}>
                    <Button
                    style ={{margin:15, marginTop: 0}}
                    icon = "pencil"
                    mode="contained"
                    onPress={()=> props.navigation.navigate("Edit", {data:data})}
                        >
                    Edit
                    </Button>
                    <Button
                    style ={{margin:15, marginTop: 0}}
                    icon = "delete"
                    mode="contained"
                    onPress={()=> console.log('pressed')}
                        >
                    Delete
                    </Button>
                </View>

            </View>

        </ScrollView>
    )
}

export default Details

const styles = StyleSheet.create({
    viewStyle: {
        padding: 10,
        margin: 10,

    },
    btnStyle: {
        flexDirection: "row",
        justifyContent: "space-evenly",
        margin: 15,
        padding: 10
    },
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