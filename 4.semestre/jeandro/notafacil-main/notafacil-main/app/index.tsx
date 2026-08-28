import type { Nota } from "@/types";
import { useLocalSearchParams, useRouter } from "expo-router";
import { useEffect, useState } from "react";
import { FlatList, StyleSheet, Text, TouchableOpacity, View } from "react-native";
 
const notasIniciais: Nota[] = [
  { id: '1', descricaoProduto: 'Televisão 50 polegadas', loja: 'Eletro Sul' },
  { id: '2', descricaoProduto: 'Notebook Dell', loja: 'Info Center' },
  { id: '3', descricaoProduto: 'Liquidificador', loja: 'Casa e Cia' },
];
 
export default function ListagemScreen() {
  const router = useRouter();
  const { novaNota, notaEditada } = useLocalSearchParams<{ novaNota?: string; notaEditada?: string }>();
  const [notas, setNotas] = useState<Nota[]>(notasIniciais);
 
  // Quando a tela de Cadastro volta com uma nova nota ou uma nota editada,
  // atualizamos a lista e limpamos o parâmetro.
  useEffect(() => {
    if (novaNota) {
      const nota: Nota = JSON.parse(novaNota);
      setNotas((atual) => [...atual, nota]);
      router.setParams({ novaNota: undefined });
    }
    if (notaEditada) {
      const nota: Nota = JSON.parse(notaEditada);
      setNotas((atual) => atual.map((n) => (n.id === nota.id ? nota : n)));
      router.setParams({ notaEditada: undefined });
    }
  }, [novaNota, notaEditada]);
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>NotaFácil</Text>
        <TouchableOpacity onPress={() => router.push('/cadastro')}>
          <Text style={styles.addButton}>+</Text>
        </TouchableOpacity>
      </View>
 
      <FlatList
        data={notas}
        keyExtractor={(item) => item.id}
        contentContainerStyle={{ padding: 12 }}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.card}
            onPress={() => router.push({ pathname: '/cadastro', params: { nota: JSON.stringify(item) } })}
          >
            <Text style={styles.cardTitle}>{item.descricaoProduto}</Text>
            <Text style={styles.cardSubtitle}>{item.loja}</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
}
 
const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0E1B33' },
  header: {
    backgroundColor: '#D85A30', padding: 16,
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center',
  },
  headerTitle: { color: '#FAECE7', fontSize: 20, fontWeight: 'bold' },
  addButton: { color: '#FAECE7', fontSize: 26, fontWeight: 'bold' },
  card: {
    backgroundColor: '#16264A', borderRadius: 10, padding: 14, marginBottom: 10,
    borderWidth: 1, borderColor: '#223564',
  },
  cardTitle: { color: '#F0F2FA', fontSize: 15, fontWeight: 'bold' },
  cardSubtitle: { color: '#98A4C8', fontSize: 13, marginTop: 2 },
});
