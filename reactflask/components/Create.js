import React, {useState} from 'react'
import {View, Text, StyleSheet} from 'react-native'
import {TextInput, Button} from 'react-native-paper'

function Create(props) {
    const [title, setTitle] = useState("")
    const [body, setBody] = useState("")

    const insertData = () =>{
        fetch('http://192.168.0.4:3000/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({title:title, body:body})
        })
        .then(resp => resp.json())
        .then(data => {
            props.navigation.navigate('Home')
        })
        .catch(function(error){
            console.log("error with fetch:" + error.message);
            //throws error
            throw error;
        })
    }

    return (
        <View>
            <TextInput style = {styles.InputStyle} style ={{margin:10}}
            label = "Title"
            value = {title}
            mode="outlined"
            onChangeText = {text => setTitle(text)}/>
            <TextInput style = {styles.InputStyle} style ={{marginRight:15, marginLeft:15,marginBottom:10} }
            label = "Description"
            value = {body}
            multiline
            numberOfLines = {10}
            mode="outlined"
            onChangeText = {text => setBody(text)}/>
            <Button
            style ={{margin:15, marginTop: 0}}
            icon = "pencil"
            mode="contained"
            onPress={()=> insertData()}
            >Insert Article</Button>
        </View>

    )
}
const styles = StyleSheet.create({
    inputStyle: {
        marginTop:10,
    }
})


export default Create