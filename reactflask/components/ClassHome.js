import React, { Component } from 'react'
import {StyleSheet, View, Text, Button} from 'react-native'

class ClassHome extends Component {

    state = {
        name: "Erik"
    }

    render() {
        return (
            <View>
            <Text style={styles.textStyle}>Howdy, from the Class</Text>
            <Text style={styles.textStyle}>{this.state.name}</Text>
            <Button style={styles.buttonStyle}title="Click Me!" onPress={()=> this.setState({name: "This is changed"})}/>
            </View>
        )
    }
}

export default ClassHome

const styles = StyleSheet.create({
    textStyle: {
        color: 'white',
        backgroundColor: 'green',
        padding: 20,
        margin: 20,
        fontSize: 20,
    },
    buttonStyle: {
        color: 'lightblue',
        backgroundColor:'green',
        paddingTop: 20
    }
  });